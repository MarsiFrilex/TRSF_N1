from src.repositories.objects_repository import ObjectsRepository
from src.schemas.objects_schemas import CreateObjectSchema, UpdateObjectSchema


class ObjectsService:
    def __init__(self, repository: ObjectsRepository):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def get(self, object_id: int):
        return await self.repository.get(object_id=object_id)

    async def create(self, obj: CreateObjectSchema):
        return await self.repository.create(obj=obj)

    async def update(self, object_id: int, obj: UpdateObjectSchema):
        return await self.repository.update(object_id=object_id, obj=obj)

    async def delete(self, object_id: int):
        return await self.repository.delete(object_id=object_id)
