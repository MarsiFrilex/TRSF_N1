from fastapi import APIRouter, Depends

from src.api.dependencies import get_objects_service
from src.schemas.objects_schemas import CreateObjectSchema, UpdateObjectSchema
from src.services.objects_service import ObjectsService

router = APIRouter(
    prefix="/objects",
    tags=["Objects"]
)


@router.post("")
async def create_object(
        obj: CreateObjectSchema,
        objects_service: ObjectsService = Depends(get_objects_service),
):
    return await objects_service.create(obj)


@router.get("")
async def get_objects(
        objects_service: ObjectsService = Depends(get_objects_service),
):
    return await objects_service.get_all()


@router.patch("/{object_id}")
async def update_object(
        object_id: int,
        obj: UpdateObjectSchema,
        objects_service: ObjectsService = Depends(get_objects_service),
):
    return await objects_service.update(object_id, obj)


@router.delete("/{object_id}")
async def delete_object(
        object_id: int,
        objects_service: ObjectsService = Depends(get_objects_service),
):
    return await objects_service.delete(object_id)