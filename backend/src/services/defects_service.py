from src.repositories.defects_repository import DefectsRepository
from src.schemas.defects_schemas import CreateDefectSchema, UpdateDefectSchema


class DefectsService:
    def __init__(self, repository: DefectsRepository):
        self.repository = repository

    async def get_all(self, object_id: int = None, status_id: int = None):
        return await self.repository.get_all(object_id=object_id, status_id=status_id)

    async def get(self, defect_id: int):
        return await self.repository.get(defect_id=defect_id)

    async def create(self, defect: CreateDefectSchema):
        return await self.repository.create(defect=defect)

    async def update(self, defect_id: int, defect: UpdateDefectSchema):
        return await self.repository.update(defect_id=defect_id, defect=defect)

    async def delete(self, defect_id: int):
        return await self.repository.delete(defect_id=defect_id)
