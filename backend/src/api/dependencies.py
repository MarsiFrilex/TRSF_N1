from src.repositories.auth_repository import AuthRepository
from src.repositories.users_repository import UsersRepository
from src.services.auth_service import AuthService


async def get_auth_service() -> AuthService:
    return AuthService(AuthRepository(), UsersRepository())