"""
Configuración de la aplicación - Carga variables de entorno.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración central del backend."""

    # MongoDB
    mongo_uri: str = "mongodb://admin:acuaponia2026@mongo:27017/acuaponia?authSource=admin"
    mongo_db_name: str = "acuaponia"

    # MQTT
    mqtt_broker_host: str = "emqx"
    mqtt_broker_port: int = 1883
    mqtt_base_topic: str = "acuaponia"

    # Sistema
    system_id: str = "sistema-01"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    cors_origins: str = "http://localhost:3000,http://localhost:80,http://frontend:80"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
