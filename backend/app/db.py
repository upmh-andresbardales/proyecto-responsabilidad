"""
Inicialización de la base de datos MongoDB con Beanie.
"""

from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie

from app.config import settings
from app.models.sensor import Alert, SensorReading
from app.models.user import User
from app.services.user_seed import ensure_test_users

# Cliente global de MongoDB
_client: AsyncIOMotorClient | None = None


async def init_db():
    """Inicializar la conexión a MongoDB y registrar modelos Beanie."""
    global _client
    print(f"[DB] Conectando a MongoDB: {settings.mongo_uri}")

    _client = AsyncIOMotorClient(settings.mongo_uri)
    db = _client[settings.mongo_db_name]

    await init_beanie(
        database=db,
        document_models=[SensorReading, Alert, User],
    )
    await ensure_test_users()
    print(f"[DB] Conexion exitosa a base de datos '{settings.mongo_db_name}'")


async def close_db():
    """Cerrar la conexión a MongoDB."""
    global _client
    if _client:
        _client.close()
        print("[DB] Conexion a MongoDB cerrada")
