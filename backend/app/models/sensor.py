"""
Modelos de datos para el sistema acuapónico.
Usa Beanie (ODM para MongoDB) con Pydantic.
"""

from datetime import datetime, timezone
from typing import Optional

from beanie import Document
from pydantic import BaseModel, Field


class SensorReading(Document):
    """Lectura individual de un sensor."""

    sensor_id: str = Field(..., description="Identificador del sensor (ej: ph-01)")
    sensor_type: str = Field(..., description="Tipo de sensor (ej: ph, temperatura_agua)")
    value: float = Field(..., description="Valor de la lectura")
    unit: str = Field(..., description="Unidad de medida")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    system_id: str = Field(default="sistema-01")

    class Settings:
        name = "sensor_readings"
        indexes = [
            "sensor_type",
            "system_id",
            [("sensor_type", 1), ("timestamp", -1)],
            [("system_id", 1), ("sensor_type", 1), ("timestamp", -1)],
        ]


class Alert(Document):
    """Alerta generada cuando un sensor excede los umbrales."""

    alert_id: str = Field(..., description="Identificador único de la alerta")
    sensor_type: str = Field(..., description="Tipo de sensor que generó la alerta")
    sensor_id: str = Field(..., description="ID del sensor")
    value: float = Field(..., description="Valor que disparó la alerta")
    threshold: float = Field(..., description="Umbral excedido")
    severity: str = Field(..., description="Severidad: info, warning, critical")
    message: str = Field(..., description="Descripción de la alerta")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    system_id: str = Field(default="sistema-01")
    acknowledged: bool = Field(default=False, description="Si la alerta fue reconocida")

    class Settings:
        name = "alerts"
        indexes = [
            "severity",
            "sensor_type",
            [("timestamp", -1)],
            [("system_id", 1), ("acknowledged", 1), ("timestamp", -1)],
        ]


class SensorReadingResponse(BaseModel):
    """Esquema de respuesta para lecturas de sensores."""

    sensor_id: str
    sensor_type: str
    value: float
    unit: str
    timestamp: datetime
    system_id: str


class AlertResponse(BaseModel):
    """Esquema de respuesta para alertas."""

    alert_id: str
    sensor_type: str
    sensor_id: str
    value: float
    threshold: float
    severity: str
    message: str
    timestamp: datetime
    system_id: str
    acknowledged: bool


class SensorStats(BaseModel):
    """Estadísticas de un sensor."""

    sensor_type: str
    avg: float
    min: float
    max: float
    count: int
    last_value: Optional[float] = None
    last_timestamp: Optional[datetime] = None
