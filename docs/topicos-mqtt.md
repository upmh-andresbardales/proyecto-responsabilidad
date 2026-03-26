# 📡 Documentación de Tópicos MQTT - Sistema Acuapónico

## Jerarquía de Tópicos

```
acuaponia/{system_id}/sensor/{sensor_type}/data      → Datos de telemetría
acuaponia/{system_id}/sensor/{sensor_type}/status     → Estado del sensor
acuaponia/{system_id}/actuator/{actuator_type}/cmd    → Comandos a actuadores
acuaponia/{system_id}/actuator/{actuator_type}/status → Estado de actuadores
acuaponia/{system_id}/alert                           → Alertas del sistema
```
/relevador1
## Tópicos de Sensores

| # | Sensor | Tópico Completo | QoS |
|---|--------|----------------|-----|
| 1 | pH | `acuaponia/sistema-01/sensor/ph/data` | 1 |
| 2 | Temperatura del Agua | `acuaponia/sistema-01/sensor/temperatura_agua/data` | 1 |
| 3 | Oxígeno Disuelto | `acuaponia/sistema-01/sensor/oxigeno_disuelto/data` | 1 |
| 4 | Nivel de Agua | `acuaponia/sistema-01/sensor/nivel_agua/data` | 1 |
| 5 | Temperatura Ambiente | `acuaponia/sistema-01/sensor/temperatura_ambiente/data` | 1 |
| 6 | Humedad Ambiente | `acuaponia/sistema-01/sensor/humedad_ambiente/data` | 1 |
| 7 | Conductividad Eléctrica | `acuaponia/sistema-01/sensor/conductividad_electrica/data` | 1 |
| 8 | Turbidez | `acuaponia/sistema-01/sensor/turbidez/data` | 1 |
| 9 | Presión Atmosférica | `acuaponia/sistema-01/sensor/presion_atmosferica/data` | 1 |
| 10 | Flujo de Agua | `acuaponia/sistema-01/sensor/flujo_agua/data` | 1 |

## Tópico de Alertas

| Tópico | Descripción |
|--------|------------|
| `acuaponia/sistema-01/alert` | Alertas generadas automáticamente cuando un sensor excede umbrales |

## Suscripciones con Wildcards

```bash
# Todos los sensores de un sistema
acuaponia/sistema-01/sensor/+/data

# Todo de un sistema específico
acuaponia/sistema-01/#

# Todos los sistemas, todos los sensores
acuaponia/+/sensor/+/data
```

## Formato del Payload (JSON)

### Datos de Sensor
```json
{
  "sensor_id": "ph-01",
  "value": 7.2,
  "unit": "pH",
  "timestamp": "2026-03-11T20:00:00Z",
  "system_id": "sistema-01"
}
```

### Alerta
```json
{
  "alert_id": "alert-001",
  "sensor_type": "ph",
  "sensor_id": "ph-01",
  "value": 9.5,
  "threshold": 9.0,
  "severity": "critical",
  "message": "pH fuera de rango critico: 9.5 (umbral: > 9.0)",
  "timestamp": "2026-03-11T20:05:00Z",
  "system_id": "sistema-01"
}
```

## Broker EMQX

- **Dashboard**: http://localhost:18083
- **Credenciales**: admin / public
- **Puerto MQTT**: 1883
- **Puerto WebSocket**: 8083 (usado por el frontend Vue)
