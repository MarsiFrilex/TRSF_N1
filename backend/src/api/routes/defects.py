from fastapi import APIRouter, Depends

from src.api.dependencies import get_defects_service
from src.schemas.defects_schemas import CreateDefectSchema, UpdateDefectSchema
from src.services.defects_service import DefectsService

router = APIRouter(
    prefix="/defects",
    tags=["Defects"]
)


@router.post("")
async def create_defect(
        defect: CreateDefectSchema,
        defects_service: DefectsService = Depends(get_defects_service),
):
    return await defects_service.create(defect)


@router.get("")
async def get_defects(
        object_id_filter: int | None = None,
        status_id_filter: int | None = None,
        defects_service: DefectsService = Depends(get_defects_service),
):
    return await defects_service.get_all(object_id_filter, status_id_filter)


@router.get("/{defect_id}")
async def get_defect(
        defect_id: int,
        defects_service: DefectsService = Depends(get_defects_service),
):
    return await defects_service.get(defect_id)


@router.patch("/{defect_id}")
async def update_defect(
        defect_id: int,
        defect: UpdateDefectSchema,
        defects_service: DefectsService = Depends(get_defects_service),
):
    return await defects_service.update(defect_id, defect)


@router.delete("/{defect_id}")
async def delete_defect(
        defect_id: int,
        defects_service: DefectsService = Depends(get_defects_service),
):
    return await defects_service.delete(defect_id)