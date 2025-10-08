from fastapi import APIRouter, Depends

from src.api.dependencies import get_roles_service
from src.services.roles_service import RolesService

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post("", summary="Создать новую роль")
async def create_role(
        role_name: str,
        roles_service: RolesService = Depends(get_roles_service),
):
    return await roles_service.create(role_name)


@router.get("", summary="Получить список всех ролей")
async def get_roles(
        roles_service: RolesService = Depends(get_roles_service),
):
    return await roles_service.get_all()


@router.delete("/{role_id}", summary="Удалить роль")
async def delete_role(
        role_id: int,
        roles_service: RolesService = Depends(get_roles_service),
):
    return await roles_service.delete(role_id)