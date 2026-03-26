"""
Modelos de usuario para autenticacion basica.
"""

from datetime import datetime, timezone

from beanie import Document
from pydantic import BaseModel, Field


class User(Document):
    """Usuario del sistema."""

    username: str = Field(..., description="Nombre de usuario unico")
    full_name: str = Field(..., description="Nombre completo")
    email: str = Field(..., description="Correo de usuario")
    password_hash: str = Field(..., description="Hash de la contrasena")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"
        indexes = [
            "username",
            "email",
        ]


class UserResponse(BaseModel):
    """Esquema de salida para usuarios."""

    username: str
    full_name: str
    email: str
    is_active: bool


class LoginRequest(BaseModel):
    """Payload de autenticacion."""

    username: str
    password: str


class LoginResponse(BaseModel):
    """Respuesta simple de autenticacion."""

    success: bool
    message: str
    user: UserResponse | None = None