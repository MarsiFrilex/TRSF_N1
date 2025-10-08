from fastapi import APIRouter, Depends

from src.api.dependencies import get_auth_service
from src.schemas.auth_schemas import RefreshToken, Login
from src.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post('/login', summary="Вход в аккаунт")
async def user_login(login_form: Login, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.login(login_form.email, login_form.password)


@router.post('/refresh', summary="Обновление refresh-токена")
async def token_refresh(refresh_token: RefreshToken, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.refresh_token(refresh_token.token)