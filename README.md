# 🌿 Sistema de Monitoreo Acuapónico Inteligente

Sistema de monitoreo en tiempo real para sistemas acuapónicos, con capacidad de predicción mediante IA. Diseñado como plataforma agnóstica a la fuente de datos (sintéticos o sensores reales vía ESP32/Raspberry Pi).

## 📋 Descripción

Este proyecto implementa una plataforma completa de monitoreo IoT para acuaponía que incluye:

- **Broker MQTT (EMQX)**: Gestión de mensajería IoT en tiempo real
- **Backend (FastAPI)**: API REST + suscriptor MQTT para persistencia y lógica de negocio
- **Base de datos (MongoDB)**: Almacenamiento de telemetría y alertas
- **Frontend (Vue 3)**: Dashboard de visualización con gauges y gráficas temporales
- **Simulador**: Generador de datos sintéticos para desarrollo y pruebas

## 🏗️ Stack Tecnológico

| Componente | Tecnología | Puerto |
|------------|-----------|--------|
| Broker MQTT | EMQX | 1883 (MQTT), 8083 (WebSocket), 18083 (Dashboard) |
| Base de Datos | MongoDB | 27017 |
| Backend API | FastAPI + Python 3.12 | 8000 |
| Frontend | Vue 3 + Vite + TypeScript | 3000 |
| Simulador | Python + paho-mqtt | - |

## 🚀 Instalación Rápida

### Prerrequisitos
- [Docker](https://docs.docker.com/get-docker/) (v20+)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2+)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/upmh-andresbardales/proyecto-responsabilidad.git
cd proyecto-responsabilidad

# 2. Copiar variables de entorno
cp .env.example .env

# 3. Levantar todos los servicios
docker compose up --build

# 4. ¡Listo! Acceder a los servicios:
```

### URLs de Acceso

| Servicio | URL | Credenciales |
|----------|-----|-------------|
| Dashboard EMQX | http://localhost:18083 | admin / public |
| API Swagger | http://localhost:8000/docs | - |
| Frontend Dashboard | http://localhost:3000 | - |

## 📡 Sensores Monitoreados

| Sensor | Rango Normal | Unidad | Umbral Crítico |
|--------|-------------|--------|----------------|
| pH | 6.0 - 8.5 | pH | < 5.5 o > 9.0 |
| Temperatura del Agua | 18 - 30 | °C | < 15 o > 35 |
| Oxígeno Disuelto | 5.0 - 9.0 | mg/L | < 4.0 |
| Nivel de Agua | 30 - 100 | cm | < 20 |
| Temperatura Ambiente | 15 - 40 | °C | < 10 o > 45 |
| Humedad Ambiente | 40 - 80 | % | < 30 o > 90 |
| Conductividad Eléctrica | 0.5 - 3.0 | mS/cm | < 0.3 o > 4.0 |
| Turbidez | 0 - 50 | NTU | > 100 |
| Presión Atmosférica | 950 - 1050 | hPa | < 900 o > 1100 |
| Flujo de Agua | 1.0 - 10.0 | L/min | < 0.5 |

## 🔌 Conexión con Hardware Real

Para conectar sensores reales (ESP32/Raspberry Pi), simplemente publica datos MQTT al broker en el formato esperado:

```
Tópico: acuaponia/sistema-01/sensor/{tipo_sensor}/data
```

Payload JSON:
```json
{
  "sensor_id": "ph-01",
  "value": 7.2,
  "unit": "pH",
  "timestamp": "2026-03-11T20:00:00Z",
  "system_id": "sistema-01"
}
```

Consulta `docs/data-reference.md` para ver todos los payloads y estructuras de datos.

## 👥 Equipo

- UPMH - Maestría en Ingeniería de Software
- Materia: Responsabilidad Social
- Segundo Cuatrimestre 2026

## 📄 Licencia

Proyecto académico - Universidad Politécnica Metropolitana de Hidalgo
