from fastapi import APIRouter, Depends

from src.api.dependencies import get_tags_service
from src.services.tags_service import TagsService

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)


@router.post("")
async def create_tag(
        tag_name: str,
        tags_service: TagsService = Depends(get_tags_service),
):
    return await tags_service.create(tag_name)


@router.get("")
async def get_tags(
        tags_service: TagsService = Depends(get_tags_service),
):
    return await tags_service.get_all()


@router.delete("/{tag_id}")
async def delete_tag(
        tag_id: int,
        tags_service: TagsService = Depends(get_tags_service),
):
    return await tags_service.delete(tag_id)