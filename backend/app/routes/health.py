"""
Health Check - Endpoint de verificación del servicio.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Verificar que el backend está funcionando."""
    return {"status": "ok", "service": "acuaponia-backend"}
