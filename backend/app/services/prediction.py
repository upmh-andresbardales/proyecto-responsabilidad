"""
Servicio de predicción - Placeholder para modelo de IA.
El modelo será entrenado en Google Colab y exportado como Keras/TensorFlow.
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["Prediction"])


class PredictionRequest(BaseModel):
    """Datos de entrada para predicción."""

    ph: float
    temperatura_agua: float
    oxigeno_disuelto: float
    nivel_agua: float
    temperatura_ambiente: float
    humedad_ambiente: float
    conductividad_electrica: float
    turbidez: float
    presion_atmosferica: float
    flujo_agua: float


class PredictionResponse(BaseModel):
    """Resultado de la predicción."""

    prediction: str
    confidence: float
    recommendations: list[str]
    model_version: str


@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):
    """
    Endpoint de predicción - Placeholder.
    TODO: Cargar modelo Keras exportado desde Colab.
    Por ahora retorna un mock basado en reglas simples.
    """
    recommendations = []
    risk_level = "normal"
    confidence = 0.85

    # Reglas simples de mock
    if data.ph < 6.0 or data.ph > 8.5:
        recommendations.append(f"Ajustar pH (actual: {data.ph})")
        risk_level = "warning"
        confidence = 0.75

    if data.temperatura_agua > 30:
        recommendations.append(f"Reducir temperatura del agua (actual: {data.temperatura_agua}°C)")
        risk_level = "warning"

    if data.oxigeno_disuelto < 5.0:
        recommendations.append(f"Incrementar oxigenacion (actual: {data.oxigeno_disuelto} mg/L)")
        risk_level = "critical"
        confidence = 0.92

    if data.flujo_agua < 1.0:
        recommendations.append("Verificar bomba de agua - flujo bajo detectado")
        risk_level = "critical"
        confidence = 0.95

    if not recommendations:
        recommendations.append("Sistema operando en parametros normales")

    return PredictionResponse(
        prediction=risk_level,
        confidence=confidence,
        recommendations=recommendations,
        model_version="mock-v1.0 (pendiente modelo Keras)",
    )
