"""
Rutas de autenticacion y gestion de usuarios.
"""

from fastapi import APIRouter, HTTPException, status
from passlib.context import CryptContext
from pydantic import BaseModel

from app.models.user import LoginRequest, LoginResponse, User, UserResponse

router = APIRouter(prefix="/api", tags=["Auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    full_name: str
    email: str
    password: str


class UpdateUserRequest(BaseModel):
    full_name: str | None = None
    email: str | None = None
    is_active: bool | None = None


@router.get("/users", response_model=list[UserResponse])
async def get_users():
    """Listar usuarios de prueba disponibles."""
    users = await User.find_all().sort("username").to_list()
    return [
        UserResponse(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            is_active=user.is_active,
        )
        for user in users
    ]


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: CreateUserRequest):
    """Crear un nuevo usuario."""
    existing = await User.find_one(User.username == payload.username)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El usuario ya existe")
    user = User(
        username=payload.username,
        full_name=payload.full_name,
        email=payload.email,
        password_hash=pwd_context.hash(payload.password),
    )
    await user.insert()
    return UserResponse(username=user.username, full_name=user.full_name, email=user.email, is_active=user.is_active)


@router.get("/users/{username}", response_model=UserResponse)
async def get_user(username: str):
    """Obtener un usuario por username."""
    user = await User.find_one(User.username == username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return UserResponse(username=user.username, full_name=user.full_name, email=user.email, is_active=user.is_active)


@router.put("/users/{username}", response_model=UserResponse)
async def update_user(username: str, payload: UpdateUserRequest):
    """Actualizar datos de un usuario."""
    user = await User.find_one(User.username == username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    if payload.full_name is not None:
        user.full_name = payload.full_name
    if payload.email is not None:
        user.email = payload.email
    if payload.is_active is not None:
        user.is_active = payload.is_active
    await user.save()
    return UserResponse(username=user.username, full_name=user.full_name, email=user.email, is_active=user.is_active)


@router.delete("/users/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(username: str):
    """Eliminar un usuario."""
    user = await User.find_one(User.username == username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    await user.delete()


@router.post("/auth/login", response_model=LoginResponse)
async def login(payload: LoginRequest):
    """Validar credenciales de usuario con password hasheada."""
    user = await User.find_one(User.username == payload.username)
    if not user or not pwd_context.verify(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales invalidas",
        )

    return LoginResponse(
        success=True,
        message="Login exitoso",
        user=UserResponse(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            is_active=user.is_active,
        ),
    )