from fastapi import APIRouter, Depends

from src.api.dependencies import get_auth_service
from src.schemas.user_schemas import CreateUserSchema
from src.services.auth_service import AuthService

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)


@router.post("", summary="Создать аккаунт для сотрудника")
async def user_register(user: CreateUserSchema, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.register(user)


@router.get("", summary="Получить список пользователей")
async def user_list(auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.get_users()