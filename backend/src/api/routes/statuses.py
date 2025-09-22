from fastapi import APIRouter, Depends

from src.api.dependencies import get_statuses_service
from src.services.statuses_service import StatusesService

router = APIRouter(
    prefix="/statuses",
    tags=["Statuses"]
)


@router.post("", summary="Создать новый статус")
async def create_status(
        status_name: str,
        status_service: StatusesService = Depends(get_statuses_service),
):
    return await status_service.create(status_name)


@router.get("", summary="Получить список всех статусов")
async def get_statuses(
        status_service: StatusesService = Depends(get_statuses_service),
):
    return await status_service.get_all()


@router.delete("/{status_id}", summary="Удалить статус")
async def delete_status(
        status_id: int,
        status_service: StatusesService = Depends(get_statuses_service),
):
    return await status_service.delete(status_id)