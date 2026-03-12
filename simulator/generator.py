"""
Generador de Datos Sintéticos para Sistema Acuapónico
=====================================================
Publica datos simulados de 10 sensores vía MQTT al broker EMQX.
Soporta escenarios: normal, pico de pH, fallo de bomba, temperatura alta.
"""

import json
import math
import os
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

# ============================================
# Configuración desde variables de entorno
# ============================================
MQTT_HOST = os.getenv("MQTT_BROKER_HOST", "emqx")
MQTT_PORT = int(os.getenv("MQTT_BROKER_PORT", "1883"))
SYSTEM_ID = os.getenv("SYSTEM_ID", "sistema-01")
BASE_TOPIC = os.getenv("MQTT_BASE_TOPIC", "acuaponia")
PUBLISH_INTERVAL = int(os.getenv("SENSOR_PUBLISH_INTERVAL", "5"))

# ============================================
# Definición de sensores con rangos realistas
# ============================================
SENSORS = {
    "ph": {
        "sensor_id": "ph-01",
        "unit": "pH",
        "base_value": 7.0,
        "noise": 0.3,
        "min": 5.0,
        "max": 10.0,
        "normal_min": 6.0,
        "normal_max": 8.5,
        "critical_low": 5.5,
        "critical_high": 9.0,
    },
    "temperatura_agua": {
        "sensor_id": "temp-agua-01",
        "unit": "°C",
        "base_value": 24.0,
        "noise": 1.0,
        "min": 10.0,
        "max": 40.0,
        "normal_min": 18.0,
        "normal_max": 30.0,
        "critical_low": 15.0,
        "critical_high": 35.0,
    },
    "oxigeno_disuelto": {
        "sensor_id": "od-01",
        "unit": "mg/L",
        "base_value": 7.0,
        "noise": 0.5,
        "min": 2.0,
        "max": 12.0,
        "normal_min": 5.0,
        "normal_max": 9.0,
        "critical_low": 4.0,
        "critical_high": None,
    },
    "nivel_agua": {
        "sensor_id": "nivel-01",
        "unit": "cm",
        "base_value": 65.0,
        "noise": 5.0,
        "min": 0.0,
        "max": 120.0,
        "normal_min": 30.0,
        "normal_max": 100.0,
        "critical_low": 20.0,
        "critical_high": None,
    },
    "temperatura_ambiente": {
        "sensor_id": "temp-amb-01",
        "unit": "°C",
        "base_value": 27.0,
        "noise": 2.0,
        "min": 5.0,
        "max": 50.0,
        "normal_min": 15.0,
        "normal_max": 40.0,
        "critical_low": 10.0,
        "critical_high": 45.0,
    },
    "humedad_ambiente": {
        "sensor_id": "hum-01",
        "unit": "%",
        "base_value": 60.0,
        "noise": 5.0,
        "min": 10.0,
        "max": 100.0,
        "normal_min": 40.0,
        "normal_max": 80.0,
        "critical_low": 30.0,
        "critical_high": 90.0,
    },
    "conductividad_electrica": {
        "sensor_id": "ce-01",
        "unit": "mS/cm",
        "base_value": 1.5,
        "noise": 0.3,
        "min": 0.1,
        "max": 5.0,
        "normal_min": 0.5,
        "normal_max": 3.0,
        "critical_low": 0.3,
        "critical_high": 4.0,
    },
    "turbidez": {
        "sensor_id": "turb-01",
        "unit": "NTU",
        "base_value": 25.0,
        "noise": 8.0,
        "min": 0.0,
        "max": 200.0,
        "normal_min": 0.0,
        "normal_max": 50.0,
        "critical_low": None,
        "critical_high": 100.0,
    },
    "presion_atmosferica": {
        "sensor_id": "pres-01",
        "unit": "hPa",
        "base_value": 1013.0,
        "noise": 5.0,
        "min": 850.0,
        "max": 1100.0,
        "normal_min": 950.0,
        "normal_max": 1050.0,
        "critical_low": 900.0,
        "critical_high": 1100.0,
    },
    "flujo_agua": {
        "sensor_id": "flujo-01",
        "unit": "L/min",
        "base_value": 5.0,
        "noise": 1.0,
        "min": 0.0,
        "max": 15.0,
        "normal_min": 1.0,
        "normal_max": 10.0,
        "critical_low": 0.5,
        "critical_high": None,
    },
}

# ============================================
# Escenarios de simulación
# ============================================
SCENARIOS = [
    {
        "name": "normal",
        "weight": 70,
        "overrides": {},
    },
    {
        "name": "pico_ph",
        "weight": 10,
        "overrides": {
            "ph": {"base_value": 9.2, "noise": 0.5},
        },
    },
    {
        "name": "fallo_bomba",
        "weight": 10,
        "overrides": {
            "flujo_agua": {"base_value": 0.2, "noise": 0.1},
            "nivel_agua": {"base_value": 25.0, "noise": 3.0},
        },
    },
    {
        "name": "temperatura_alta",
        "weight": 10,
        "overrides": {
            "temperatura_agua": {"base_value": 33.0, "noise": 1.5},
            "temperatura_ambiente": {"base_value": 42.0, "noise": 2.0},
        },
    },
]


def select_scenario():
    """Seleccionar un escenario basado en pesos probabilísticos."""
    weights = [s["weight"] for s in SCENARIOS]
    return random.choices(SCENARIOS, weights=weights, k=1)[0]


def generate_value(sensor_config, time_offset):
    """
    Generar un valor realista con variación sinusoidal + ruido gaussiano.
    La onda sinusoidal simula variaciones naturales a lo largo del tiempo.
    """
    base = sensor_config["base_value"]
    noise = sensor_config["noise"]

    # Variación sinusoidal lenta (ciclo de ~5 minutos)
    sine_variation = math.sin(time_offset / 300.0 * 2 * math.pi) * noise * 0.5

    # Ruido gaussiano
    gaussian_noise = random.gauss(0, noise * 0.3)

    value = base + sine_variation + gaussian_noise

    # Clamp al rango del sensor
    value = max(sensor_config["min"], min(sensor_config["max"], value))

    return round(value, 2)


def create_payload(sensor_type, sensor_config, value):
    """Crear payload JSON para publicación MQTT."""
    return {
        "sensor_id": sensor_config["sensor_id"],
        "value": value,
        "unit": sensor_config["unit"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "system_id": SYSTEM_ID,
    }


def on_connect(client, userdata, flags, reason_code, properties):
    """Callback de conexión al broker."""
    if reason_code == 0:
        print(f"[SIMULATOR] Conectado al broker MQTT en {MQTT_HOST}:{MQTT_PORT}")
    else:
        print(f"[SIMULATOR] Error de conexion: {reason_code}")


def on_disconnect(client, userdata, flags, reason_code, properties):
    """Callback de desconexión."""
    print(f"[SIMULATOR] Desconectado del broker (rc={reason_code})")


def main():
    """Bucle principal del simulador."""
    print("=" * 60)
    print("  SIMULADOR DE DATOS ACUAPÓNICOS")
    print(f"  Broker: {MQTT_HOST}:{MQTT_PORT}")
    print(f"  Sistema: {SYSTEM_ID}")
    print(f"  Intervalo: {PUBLISH_INTERVAL}s")
    print(f"  Sensores: {len(SENSORS)}")
    print("=" * 60)

    # Crear cliente MQTT
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"simulator-{SYSTEM_ID}")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # Intentar conectar con reintentos
    max_retries = 30
    for attempt in range(max_retries):
        try:
            client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
            client.loop_start()
            break
        except Exception as e:
            print(f"[SIMULATOR] Intento {attempt + 1}/{max_retries} - Esperando broker: {e}")
            time.sleep(2)
    else:
        print("[SIMULATOR] No se pudo conectar al broker MQTT. Abortando.")
        return

    time.sleep(2)  # Dar tiempo a que se establezca la conexión

    start_time = time.time()
    iteration = 0

    try:
        while True:
            time_offset = time.time() - start_time
            scenario = select_scenario()

            if iteration % 12 == 0:  # Log cada ~60 segundos
                print(f"\n[SIMULATOR] Iteracion {iteration} | Escenario: {scenario['name']}")

            for sensor_type, sensor_config in SENSORS.items():
                # Aplicar overrides del escenario si existen
                config = {**sensor_config}
                if sensor_type in scenario["overrides"]:
                    config.update(scenario["overrides"][sensor_type])

                # Generar valor
                value = generate_value(config, time_offset)

                # Crear y publicar payload
                payload = create_payload(sensor_type, config, value)
                topic = f"{BASE_TOPIC}/{SYSTEM_ID}/sensor/{sensor_type}/data"

                result = client.publish(topic, json.dumps(payload), qos=1)

                if iteration % 12 == 0:
                    print(f"  → {sensor_type}: {value} {config['unit']}")

            iteration += 1
            time.sleep(PUBLISH_INTERVAL)

    except KeyboardInterrupt:
        print("\n[SIMULATOR] Detenido por el usuario.")
    finally:
        client.loop_stop()
        client.disconnect()
        print("[SIMULATOR] Desconectado limpiamente.")


if __name__ == "__main__":
    main()
