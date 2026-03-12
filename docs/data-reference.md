# 📋 Referencia de Datos - Sistema de Monitoreo Acuapónico

Documento de referencia para desarrolladores. Contiene todos los formatos de datos, payloads MQTT, esquemas de MongoDB y ejemplos de uso de la API.

---

## 📡 Payloads MQTT por Sensor

Todos los payloads se publican en formato JSON con la siguiente estructura base:

```json
{
  "sensor_id": "<string>",
  "value": <number>,
  "unit": "<string>",
  "timestamp": "<ISO 8601>",
  "system_id": "<string>"
}
```

### 1. pH
**Tópico:** `acuaponia/sistema-01/sensor/ph/data`
```json
{
  "sensor_id": "ph-01",
  "value": 7.2,
  "unit": "pH",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 6.0 - 8.5 | < 6.0 o > 8.5 | < 5.5 o > 9.0 |

---

### 2. Temperatura del Agua
**Tópico:** `acuaponia/sistema-01/sensor/temperatura_agua/data`
```json
{
  "sensor_id": "temp-agua-01",
  "value": 24.5,
  "unit": "°C",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 18.0 - 30.0 | < 18.0 o > 30.0 | < 15.0 o > 35.0 |

---

### 3. Oxígeno Disuelto
**Tópico:** `acuaponia/sistema-01/sensor/oxigeno_disuelto/data`
```json
{
  "sensor_id": "od-01",
  "value": 7.1,
  "unit": "mg/L",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 5.0 - 9.0 | < 5.0 | < 4.0 |

---

### 4. Nivel de Agua
**Tópico:** `acuaponia/sistema-01/sensor/nivel_agua/data`
```json
{
  "sensor_id": "nivel-01",
  "value": 65.0,
  "unit": "cm",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 30.0 - 100.0 | < 30.0 | < 20.0 |

---

### 5. Temperatura Ambiente
**Tópico:** `acuaponia/sistema-01/sensor/temperatura_ambiente/data`
```json
{
  "sensor_id": "temp-amb-01",
  "value": 27.3,
  "unit": "°C",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 15.0 - 40.0 | < 15.0 o > 40.0 | < 10.0 o > 45.0 |

---

### 6. Humedad Ambiente
**Tópico:** `acuaponia/sistema-01/sensor/humedad_ambiente/data`
```json
{
  "sensor_id": "hum-01",
  "value": 62.0,
  "unit": "%",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 40.0 - 80.0 | < 40.0 o > 80.0 | < 30.0 o > 90.0 |

---

### 7. Conductividad Eléctrica
**Tópico:** `acuaponia/sistema-01/sensor/conductividad_electrica/data`
```json
{
  "sensor_id": "ce-01",
  "value": 1.8,
  "unit": "mS/cm",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 0.5 - 3.0 | < 0.5 o > 3.0 | < 0.3 o > 4.0 |

---

### 8. Turbidez
**Tópico:** `acuaponia/sistema-01/sensor/turbidez/data`
```json
{
  "sensor_id": "turb-01",
  "value": 22.5,
  "unit": "NTU",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 0.0 - 50.0 | > 50.0 | > 100.0 |

---

### 9. Presión Atmosférica
**Tópico:** `acuaponia/sistema-01/sensor/presion_atmosferica/data`
```json
{
  "sensor_id": "pres-01",
  "value": 1013.2,
  "unit": "hPa",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 950.0 - 1050.0 | < 950.0 o > 1050.0 | < 900.0 o > 1100.0 |

---

### 10. Flujo de Agua
**Tópico:** `acuaponia/sistema-01/sensor/flujo_agua/data`
```json
{
  "sensor_id": "flujo-01",
  "value": 5.3,
  "unit": "L/min",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```
| Campo | Rango Normal | Umbral Warning | Umbral Crítico |
|-------|-------------|----------------|----------------|
| value | 1.0 - 10.0 | < 1.0 | < 0.5 (fallo de bomba) |

---

## 🚨 Payload de Alertas

**Tópico:** `acuaponia/sistema-01/alert`

```json
{
  "alert_id": "alert-a1b2c3d4",
  "sensor_type": "ph",
  "sensor_id": "ph-01",
  "value": 9.5,
  "threshold": 9.0,
  "severity": "critical",
  "message": "pH fuera de rango critico: 9.5 (umbral: > 9.0)",
  "timestamp": "2026-03-11T20:20:00Z",
  "system_id": "sistema-01"
}
```

### Severidades

| Severidad | Descripción | Ejemplo |
|-----------|------------|---------|
| `warning` | Valor fuera del rango normal pero dentro de tolerancia | pH = 8.8 (normal max: 8.5, crítico: 9.0) |
| `critical` | Valor excede umbral crítico, requiere acción inmediata | pH = 9.5 (crítico: > 9.0) |

### Ejemplos de Alertas por Escenario

#### Pico de pH
```json
{
  "alert_id": "alert-ph-001",
  "sensor_type": "ph",
  "sensor_id": "ph-01",
  "value": 9.3,
  "threshold": 9.0,
  "severity": "critical",
  "message": "ph fuera de rango critico: 9.3 > 9.0",
  "timestamp": "2026-03-11T20:25:00Z",
  "system_id": "sistema-01"
}
```

#### Fallo de Bomba (flujo bajo)
```json
{
  "alert_id": "alert-flujo-001",
  "sensor_type": "flujo_agua",
  "sensor_id": "flujo-01",
  "value": 0.2,
  "threshold": 0.5,
  "severity": "critical",
  "message": "flujo_agua fuera de rango critico: 0.2 < 0.5",
  "timestamp": "2026-03-11T20:30:00Z",
  "system_id": "sistema-01"
}
```

#### Temperatura Alta
```json
{
  "alert_id": "alert-temp-001",
  "sensor_type": "temperatura_agua",
  "sensor_id": "temp-agua-01",
  "value": 33.8,
  "threshold": 30.0,
  "severity": "warning",
  "message": "temperatura_agua fuera de rango: 33.8 > 30.0",
  "timestamp": "2026-03-11T20:35:00Z",
  "system_id": "sistema-01"
}
```

#### Oxígeno Disuelto Bajo
```json
{
  "alert_id": "alert-od-001",
  "sensor_type": "oxigeno_disuelto",
  "sensor_id": "od-01",
  "value": 3.8,
  "threshold": 4.0,
  "severity": "critical",
  "message": "oxigeno_disuelto fuera de rango critico: 3.8 < 4.0",
  "timestamp": "2026-03-11T20:40:00Z",
  "system_id": "sistema-01"
}
```

---

## 🗄️ Esquemas de MongoDB

### Colección: `sensor_readings`

```json
{
  "_id": "ObjectId('...')",
  "sensor_id": "ph-01",
  "sensor_type": "ph",
  "value": 7.2,
  "unit": "pH",
  "timestamp": "2026-03-11T20:15:30Z",
  "system_id": "sistema-01"
}
```

**Índices:**
- `sensor_type` (ascending)
- `system_id` (ascending)
- Compuesto: `(sensor_type: 1, timestamp: -1)` — para consultas de historial
- Compuesto: `(system_id: 1, sensor_type: 1, timestamp: -1)` — para filtrar por sistema

---

### Colección: `alerts`

```json
{
  "_id": "ObjectId('...')",
  "alert_id": "alert-a1b2c3d4",
  "sensor_type": "ph",
  "sensor_id": "ph-01",
  "value": 9.5,
  "threshold": 9.0,
  "severity": "critical",
  "message": "pH fuera de rango critico: 9.5 (umbral: > 9.0)",
  "timestamp": "2026-03-11T20:20:00Z",
  "system_id": "sistema-01",
  "acknowledged": false
}
```

**Índices:**
- `severity` (ascending)
- `sensor_type` (ascending)
- `timestamp` (descending)
- Compuesto: `(system_id: 1, acknowledged: 1, timestamp: -1)`

---

## 🔌 API REST - Endpoints

Base URL: `http://localhost:8000`

### Health Check
```
GET /health
```
**Respuesta:**
```json
{"status": "ok", "service": "acuaponia-backend"}
```

---

### Últimas Lecturas
```
GET /api/sensors/latest
```
**Respuesta:**
```json
[
  {
    "sensor_id": "ph-01",
    "sensor_type": "ph",
    "value": 7.2,
    "unit": "pH",
    "timestamp": "2026-03-11T20:15:30Z",
    "system_id": "sistema-01"
  },
  {
    "sensor_id": "temp-agua-01",
    "sensor_type": "temperatura_agua",
    "value": 24.5,
    "unit": "°C",
    "timestamp": "2026-03-11T20:15:30Z",
    "system_id": "sistema-01"
  }
]
```

---

### Historial de Sensor
```
GET /api/sensors/{sensor_type}/history?minutes=60&limit=200
```
**Ejemplo:** `GET /api/sensors/ph/history?minutes=30`

**Respuesta:** Array de `SensorReading` ordenado por `timestamp` descendente.

---

### Estadísticas
```
GET /api/sensors/stats?minutes=60
```
**Respuesta:**
```json
[
  {
    "sensor_type": "ph",
    "avg": 7.15,
    "min": 6.82,
    "max": 7.45,
    "count": 720,
    "last_value": 7.2,
    "last_timestamp": "2026-03-11T20:15:30Z"
  }
]
```

---

### Alertas
```
GET /api/alerts?limit=50&severity=critical
```
**Respuesta:** Array de alertas ordenado por `timestamp` descendente.

---

### Conteo de Alertas
```
GET /api/alerts/count
```
**Respuesta:**
```json
{"total": 5, "critical": 2, "warning": 3}
```

---

### Predicción (Mock)
```
POST /api/predict
```
**Body:**
```json
{
  "ph": 7.2,
  "temperatura_agua": 24.5,
  "oxigeno_disuelto": 7.0,
  "nivel_agua": 65.0,
  "temperatura_ambiente": 27.0,
  "humedad_ambiente": 60.0,
  "conductividad_electrica": 1.5,
  "turbidez": 25.0,
  "presion_atmosferica": 1013.0,
  "flujo_agua": 5.0
}
```
**Respuesta:**
```json
{
  "prediction": "normal",
  "confidence": 0.85,
  "recommendations": ["Sistema operando en parametros normales"],
  "model_version": "mock-v1.0 (pendiente modelo Keras)"
}
```

**Respuesta con anomalía:**
```json
{
  "prediction": "critical",
  "confidence": 0.95,
  "recommendations": [
    "Verificar bomba de agua - flujo bajo detectado",
    "Incrementar oxigenacion (actual: 3.5 mg/L)"
  ],
  "model_version": "mock-v1.0 (pendiente modelo Keras)"
}
```

---

## 🐳 Docker Compose - Servicios

| Servicio | Imagen | Puerto Host | Puerto Interno | Depende de |
|----------|--------|-------------|----------------|------------|
| emqx | emqx/emqx:latest | 1883, 8083, 18083 | 1883, 8083, 18083 | - |
| mongo | mongo:latest | 27017 | 27017 | - |
| simulator | ./simulator (Python 3.12) | - | - | emqx (healthy) |
| backend | ./backend (Python 3.12) | 8000 | 8000 | mongo, emqx (healthy) |
| frontend | ./frontend (Node → Nginx) | 3000 | 80 | backend |

### Levantar todo
```bash
docker compose up --build
```

### Levantar solo infra (sin frontend)
```bash
docker compose up emqx mongo simulator backend
```

### Ver logs de un servicio
```bash
docker compose logs -f simulator
docker compose logs -f backend
```

### Detener y limpiar
```bash
docker compose down
docker compose down -v  # También elimina volúmenes de datos
```

---

## 🔧 Variables de Entorno

Copiar `.env.example` a `.env` antes de ejecutar.

| Variable | Valor por Defecto | Descripción |
|----------|------------------|-------------|
| `MONGO_INITDB_ROOT_USERNAME` | admin | Usuario root de MongoDB |
| `MONGO_INITDB_ROOT_PASSWORD` | acuaponia2026 | Password root de MongoDB |
| `MONGO_INITDB_DATABASE` | acuaponia | Nombre de la base de datos |
| `EMQX_DASHBOARD_USER` | admin | Usuario del dashboard EMQX |
| `EMQX_DASHBOARD_PASSWORD` | public | Password del dashboard EMQX |
| `SYSTEM_ID` | sistema-01 | Identificador del sistema acuapónico |
| `SENSOR_PUBLISH_INTERVAL` | 5 | Segundos entre publicaciones del simulador |
| `CORS_ORIGINS` | http://localhost:3000,http://localhost:80 | Orígenes permitidos para CORS |

---

## 🔄 Escenarios de Simulación

El simulador de datos sintéticos genera 4 escenarios con diferentes pesos:

| Escenario | Probabilidad | Descripción |
|-----------|-------------|-------------|
| `normal` | 70% | Valores dentro de rangos normales |
| `pico_ph` | 10% | pH sube a ~9.2 (crítico) |
| `fallo_bomba` | 10% | Flujo cae a ~0.2 L/min, nivel de agua baja |
| `temperatura_alta` | 10% | Temperatura del agua ~33°C, ambiente ~42°C |

---

## 🔌 Conectar Hardware Real (ESP32 / Raspberry Pi)

Para reemplazar el simulador con sensores reales:

1. **Detener el simulador:**
   ```bash
   docker compose stop simulator
   ```

2. **Configurar el ESP32/Raspberry** para publicar al broker MQTT:
   - Host: IP de la máquina donde corre Docker
   - Puerto: 1883
   - Tópicos: usar la misma jerarquía (`acuaponia/sistema-01/sensor/{tipo}/data`)
   - Payload: mismo formato JSON documentado arriba

3. **El resto del sistema sigue funcionando** — el backend, MongoDB y el frontend siguen operando con los datos reales en lugar de los sintéticos.

### Ejemplo Arduino/ESP32 (pseudocódigo)
```cpp
#include <PubSubClient.h>

// Publicar lectura de pH
String payload = "{\"sensor_id\":\"ph-01\",\"value\":" + String(phValue, 2) +
                 ",\"unit\":\"pH\",\"timestamp\":\"" + getISO8601() +
                 "\",\"system_id\":\"sistema-01\"}";

client.publish("acuaponia/sistema-01/sensor/ph/data", payload.c_str());
```
