# Modelo Relacional — Sistema de Monitoreo Acuapónico

Este documento define el esquema relacional equivalente a las colecciones MongoDB utilizadas en el sistema.
El proyecto usa MongoDB con Beanie (ODM) como base de datos principal. Este modelo relacional SQL existe como referencia formal para cumplir con la actividad del marco lógico y como documentación de la estructura de datos del sistema.

## Justificación

La arquitectura del proyecto usa MongoDB porque:
- Los datos de sensores son series de tiempo con schema semi-flexible.
- MQTT produce documentos JSON que se mapean directamente a colecciones.
- Beanie (ODM) simplifica la integración con FastAPI y Pydantic.

Sin embargo, el modelo relacional equivalente se documenta aquí para:
1. Demostrar que la estructura de datos está formalizada.
2. Facilitar una futura migración si se requiere para analítica SQL.
3. Cumplir con la actividad "Modelo relacional" del plan de trabajo.

---

## Diagrama Entidad-Relación (textual)

```
┌──────────────┐      ┌──────────────────┐      ┌──────────────┐
│    users     │      │  sensor_readings │      │    alerts    │
├──────────────┤      ├──────────────────┤      ├──────────────┤
│ id       PK  │      │ id           PK  │      │ id       PK  │
│ username UQ  │      │ sensor_id        │      │ alert_id UQ  │
│ full_name    │      │ sensor_type      │      │ sensor_type  │
│ email    UQ  │      │ value            │      │ sensor_id    │
│ password_hash│      │ unit             │      │ value        │
│ is_active    │      │ timestamp        │      │ threshold    │
│ created_at   │      │ system_id        │      │ severity     │
└──────────────┘      └──────────────────┘      │ message      │
                                                 │ timestamp    │
                                                 │ system_id    │
                                                 │ acknowledged │
                                                 └──────────────┘
```

---

## DDL — PostgreSQL

```sql
-- ===========================================
-- Tabla de usuarios
-- ===========================================
CREATE TABLE users (
    id              SERIAL PRIMARY KEY,
    username        VARCHAR(100) NOT NULL UNIQUE,
    full_name       VARCHAR(255) NOT NULL,
    email           VARCHAR(255) NOT NULL UNIQUE,
    password_hash   VARCHAR(255) NOT NULL,
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);

-- ===========================================
-- Tabla de lecturas de sensores
-- ===========================================
CREATE TABLE sensor_readings (
    id              BIGSERIAL PRIMARY KEY,
    sensor_id       VARCHAR(50) NOT NULL,
    sensor_type     VARCHAR(50) NOT NULL,
    value           DOUBLE PRECISION NOT NULL,
    unit            VARCHAR(20) NOT NULL,
    timestamp       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    system_id       VARCHAR(50) NOT NULL DEFAULT 'sistema-01'
);

CREATE INDEX idx_sr_sensor_type ON sensor_readings (sensor_type);
CREATE INDEX idx_sr_system_id ON sensor_readings (system_id);
CREATE INDEX idx_sr_type_ts ON sensor_readings (sensor_type, timestamp DESC);
CREATE INDEX idx_sr_system_type_ts ON sensor_readings (system_id, sensor_type, timestamp DESC);

-- ===========================================
-- Tabla de alertas
-- ===========================================
CREATE TABLE alerts (
    id              BIGSERIAL PRIMARY KEY,
    alert_id        VARCHAR(50) NOT NULL UNIQUE,
    sensor_type     VARCHAR(50) NOT NULL,
    sensor_id       VARCHAR(50) NOT NULL,
    value           DOUBLE PRECISION NOT NULL,
    threshold       DOUBLE PRECISION NOT NULL,
    severity        VARCHAR(20) NOT NULL CHECK (severity IN ('info', 'warning', 'critical')),
    message         TEXT NOT NULL,
    timestamp       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    system_id       VARCHAR(50) NOT NULL DEFAULT 'sistema-01',
    acknowledged    BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE INDEX idx_alerts_severity ON alerts (severity);
CREATE INDEX idx_alerts_sensor_type ON alerts (sensor_type);
CREATE INDEX idx_alerts_ts ON alerts (timestamp DESC);
CREATE INDEX idx_alerts_system_ack_ts ON alerts (system_id, acknowledged, timestamp DESC);
```

---

## Mapeo MongoDB ↔ SQL

| Colección MongoDB    | Tabla SQL          | Notas                                                        |
|---------------------|--------------------|--------------------------------------------------------------|
| `sensor_readings`   | `sensor_readings`  | Esquema idéntico; índices compuestos replicados               |
| `alerts`            | `alerts`           | Se agrega constraint CHECK en severity                        |
| `users`             | `users`            | Se agrega UNIQUE en username y email con índices explícitos   |

## Tópicos MQTT que alimentan estas tablas

Los datos llegan al backend vía MQTT y el servicio `mqtt_client.py` los persiste automáticamente:

| Tópico MQTT                                          | Tabla destino      |
|------------------------------------------------------|--------------------|
| `acuaponia/{system_id}/sensor/{sensor_type}/data`    | `sensor_readings`  |
| `acuaponia/{system_id}/alert`                        | `alerts`           |

Cada mensaje MQTT se transforma en un documento MongoDB equivalente a una fila SQL y se inserta en la colección correspondiente.
