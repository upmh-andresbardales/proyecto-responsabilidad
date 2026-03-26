"""
Seed de usuarios de prueba para el proyecto.
"""

from passlib.context import CryptContext

from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

TEST_USERS = [
    {
        "username": "andres",
        "full_name": "Jose Andres Bardales Calva",
        "email": "andres@optimind.local",
    },
    {
        "username": "david",
        "full_name": "David Olvera Gonzalez",
        "email": "david@optimind.local",
    },
    {
        "username": "misael",
        "full_name": "Misael Martin Lopez",
        "email": "misael@optimind.local",
    },
    {
        "username": "mauro",
        "full_name": "Mauro Alberto Ramos Angeles",
        "email": "mauro@optimind.local",
    },
]

DEFAULT_TEST_PASSWORD = "OptiMind2026!"


async def ensure_test_users():
    """Crear usuarios de prueba si aun no existen."""
    for test_user in TEST_USERS:
        existing_user = await User.find_one(User.username == test_user["username"])
        if existing_user:
            continue

        user = User(
            username=test_user["username"],
            full_name=test_user["full_name"],
            email=test_user["email"],
            password_hash=pwd_context.hash(DEFAULT_TEST_PASSWORD),
            is_active=True,
        )
        await user.insert()