"""
Endpoints REST para sensores y alertas.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional

from beanie import SortDirection
from fastapi import APIRouter, Query

from app.models.sensor import Alert, AlertResponse, SensorReading, SensorReadingResponse, SensorStats

router = APIRouter(prefix="/api", tags=["Sensors"])


@router.get("/sensors/latest", response_model=list[SensorReadingResponse])
async def get_latest_readings():
    """Obtener la última lectura de cada tipo de sensor."""
    pipeline = [
        {"$sort": {"timestamp": -1}},
        {
            "$group": {
                "_id": "$sensor_type",
                "sensor_id": {"$first": "$sensor_id"},
                "sensor_type": {"$first": "$sensor_type"},
                "value": {"$first": "$value"},
                "unit": {"$first": "$unit"},
                "timestamp": {"$first": "$timestamp"},
                "system_id": {"$first": "$system_id"},
            }
        },
        {"$sort": {"sensor_type": 1}},
    ]
    col = SensorReading.get_pymongo_collection()
    cursor = col.aggregate(pipeline)
    results = await cursor.to_list(length=100)
    return results


@router.get("/sensors/{sensor_type}/history", response_model=list[SensorReadingResponse])
async def get_sensor_history(
    sensor_type: str,
    minutes: int = Query(default=60, ge=1, le=1440, description="Minutos de historial"),
    limit: int = Query(default=200, ge=1, le=1000, description="Máximo de registros"),
):
    """Obtener historial de un sensor específico."""
    since = datetime.now(timezone.utc) - timedelta(minutes=minutes)

    readings = (
        await SensorReading.find(
            SensorReading.sensor_type == sensor_type,
            SensorReading.timestamp >= since,
        )
        .sort([("timestamp", SortDirection.DESCENDING)])
        .limit(limit)
        .to_list()
    )
    return readings


@router.get("/sensors/stats", response_model=list[SensorStats])
async def get_sensor_stats(
    minutes: int = Query(default=60, ge=1, le=1440, description="Minutos para calcular estadísticas"),
):
    """Obtener estadísticas (promedio, min, max) por sensor."""
    since = datetime.now(timezone.utc) - timedelta(minutes=minutes)

    pipeline = [
        {"$match": {"timestamp": {"$gte": since}}},
        {
            "$group": {
                "_id": "$sensor_type",
                "sensor_type": {"$first": "$sensor_type"},
                "avg": {"$avg": "$value"},
                "min": {"$min": "$value"},
                "max": {"$max": "$value"},
                "count": {"$sum": 1},
                "last_value": {"$last": "$value"},
                "last_timestamp": {"$last": "$timestamp"},
            }
        },
        {"$sort": {"sensor_type": 1}},
    ]
    col = SensorReading.get_pymongo_collection()
    cursor = col.aggregate(pipeline)
    results = await cursor.to_list(length=100)

    return [
        SensorStats(
            sensor_type=r["sensor_type"],
            avg=round(r["avg"], 2),
            min=round(r["min"], 2),
            max=round(r["max"], 2),
            count=r["count"],
            last_value=round(r.get("last_value", 0), 2),
            last_timestamp=r.get("last_timestamp"),
        )
        for r in results
    ]


@router.get("/alerts", response_model=list[AlertResponse])
async def get_alerts(
    limit: int = Query(default=50, ge=1, le=200),
    severity: Optional[str] = Query(default=None, description="Filtrar por severidad: warning, critical"),
):
    """Obtener alertas recientes."""
    query = {}
    if severity:
        query = Alert.severity == severity
        alerts = (
            await Alert.find(query)
            .sort([("timestamp", SortDirection.DESCENDING)])
            .limit(limit)
            .to_list()
        )
    else:
        alerts = (
            await Alert.find()
            .sort([("timestamp", SortDirection.DESCENDING)])
            .limit(limit)
            .to_list()
        )
    return alerts


@router.get("/alerts/count")
async def get_alert_count():
    """Obtener conteo de alertas activas (no reconocidas)."""
    total = await Alert.find(Alert.acknowledged == False).count()
    critical = await Alert.find(
        Alert.acknowledged == False, Alert.severity == "critical"
    ).count()
    warning = await Alert.find(
        Alert.acknowledged == False, Alert.severity == "warning"
    ).count()

    return {"total": total, "critical": critical, "warning": warning}
