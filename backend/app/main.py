"""
FastAPI - Punto de entrada principal.
Sistema de Monitoreo Acuapónico Inteligente.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ciclo de vida de la aplicación: startup y shutdown."""
    print("[BACKEND] Iniciando Sistema de Monitoreo Acuapónico...")
    yield
    print("[BACKEND] Cerrando sistema...")


app = FastAPI(
    title="Sistema de Monitoreo Acuapónico",
    description="API para monitoreo en tiempo real de variables acuapónicas con soporte MQTT e IA.",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
origins = [o.strip() for o in settings.cors_origins.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router, tags=["Health"])
