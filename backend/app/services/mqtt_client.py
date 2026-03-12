"""
Cliente MQTT - Suscriptor que persiste telemetría en MongoDB.
Detecta valores fuera de rango y genera alertas automáticamente.
"""

import asyncio
import json
import uuid
from datetime import datetime, timezone

import aiomqtt

from app.config import settings
from app.models.sensor import Alert, SensorReading

# ============================================
# Umbrales por tipo de sensor
# ============================================
SENSOR_THRESHOLDS = {
    "ph": {"critical_low": 5.5, "critical_high": 9.0, "warning_low": 6.0, "warning_high": 8.5},
    "temperatura_agua": {"critical_low": 15.0, "critical_high": 35.0, "warning_low": 18.0, "warning_high": 30.0},
    "oxigeno_disuelto": {"critical_low": 4.0, "critical_high": None, "warning_low": 5.0, "warning_high": 9.0},
    "nivel_agua": {"critical_low": 20.0, "critical_high": None, "warning_low": 30.0, "warning_high": 100.0},
    "temperatura_ambiente": {"critical_low": 10.0, "critical_high": 45.0, "warning_low": 15.0, "warning_high": 40.0},
    "humedad_ambiente": {"critical_low": 30.0, "critical_high": 90.0, "warning_low": 40.0, "warning_high": 80.0},
    "conductividad_electrica": {"critical_low": 0.3, "critical_high": 4.0, "warning_low": 0.5, "warning_high": 3.0},
    "turbidez": {"critical_low": None, "critical_high": 100.0, "warning_low": None, "warning_high": 50.0},
    "presion_atmosferica": {"critical_low": 900.0, "critical_high": 1100.0, "warning_low": 950.0, "warning_high": 1050.0},
    "flujo_agua": {"critical_low": 0.5, "critical_high": None, "warning_low": 1.0, "warning_high": 10.0},
}


def check_thresholds(sensor_type: str, value: float) -> tuple[str | None, float | None]:
    """
    Verificar si un valor excede los umbrales definidos.
    Retorna (severity, threshold) o (None, None) si está en rango.
    """
    thresholds = SENSOR_THRESHOLDS.get(sensor_type)
    if not thresholds:
        return None, None

    # Verificar umbrales críticos
    if thresholds["critical_low"] is not None and value < thresholds["critical_low"]:
        return "critical", thresholds["critical_low"]
    if thresholds["critical_high"] is not None and value > thresholds["critical_high"]:
        return "critical", thresholds["critical_high"]

    # Verificar umbrales de advertencia
    if thresholds["warning_low"] is not None and value < thresholds["warning_low"]:
        return "warning", thresholds["warning_low"]
    if thresholds["warning_high"] is not None and value > thresholds["warning_high"]:
        return "warning", thresholds["warning_high"]

    return None, None


async def process_message(client: aiomqtt.Client, topic: str, payload: dict):
    """Procesar un mensaje MQTT: persistir lectura y generar alertas si es necesario."""
    try:
        # Extraer el tipo de sensor del tópico
        # Formato: acuaponia/sistema-01/sensor/{sensor_type}/data
        topic_parts = topic.split("/")
        if len(topic_parts) < 5:
            return
        sensor_type = topic_parts[3]

        # Crear y guardar lectura
        reading = SensorReading(
            sensor_id=payload.get("sensor_id", "unknown"),
            sensor_type=sensor_type,
            value=payload["value"],
            unit=payload.get("unit", ""),
            timestamp=datetime.fromisoformat(payload["timestamp"]) if "timestamp" in payload else datetime.now(timezone.utc),
            system_id=payload.get("system_id", settings.system_id),
        )
        await reading.insert()

        # Verificar umbrales
        severity, threshold = check_thresholds(sensor_type, payload["value"])
        if severity:
            alert = Alert(
                alert_id=f"alert-{uuid.uuid4().hex[:8]}",
                sensor_type=sensor_type,
                sensor_id=payload.get("sensor_id", "unknown"),
                value=payload["value"],
                threshold=threshold,
                severity=severity,
                message=f"{sensor_type} fuera de rango ({severity}): {payload['value']} {payload.get('unit', '')} (umbral: {threshold})",
                timestamp=datetime.now(timezone.utc),
                system_id=payload.get("system_id", settings.system_id),
            )
            await alert.insert()

            # Publicar alerta por MQTT
            alert_topic = f"{settings.mqtt_base_topic}/{settings.system_id}/alert"
            alert_payload = {
                "alert_id": alert.alert_id,
                "sensor_type": sensor_type,
                "sensor_id": alert.sensor_id,
                "value": alert.value,
                "threshold": alert.threshold,
                "severity": alert.severity,
                "message": alert.message,
                "timestamp": alert.timestamp.isoformat(),
                "system_id": alert.system_id,
            }
            await client.publish(alert_topic, json.dumps(alert_payload), qos=1)
            print(f"[MQTT] ALERTA {severity.upper()}: {alert.message}")

    except Exception as e:
        print(f"[MQTT] Error procesando mensaje: {e}")


async def mqtt_subscriber():
    """
    Suscriptor MQTT principal. Se conecta al broker y escucha
    todos los datos de sensores para persistirlos en MongoDB.
    """
    subscribe_topic = f"{settings.mqtt_base_topic}/+/sensor/+/data"

    while True:
        try:
            print(f"[MQTT] Conectando a {settings.mqtt_broker_host}:{settings.mqtt_broker_port}...")
            async with aiomqtt.Client(
                hostname=settings.mqtt_broker_host,
                port=settings.mqtt_broker_port,
                identifier=f"backend-{settings.system_id}",
            ) as client:
                await client.subscribe(subscribe_topic, qos=1)
                print(f"[MQTT] Suscrito a: {subscribe_topic}")

                async for message in client.messages:
                    try:
                        payload = json.loads(message.payload.decode())
                        topic = str(message.topic)
                        await process_message(client, topic, payload)
                    except json.JSONDecodeError:
                        print(f"[MQTT] Payload invalido: {message.payload}")

        except aiomqtt.MqttError as e:
            print(f"[MQTT] Error de conexion: {e}. Reintentando en 5s...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"[MQTT] Error inesperado: {e}. Reintentando en 5s...")
            await asyncio.sleep(5)
