from src.repositories.tags_repository import TagsRepository


class TagsService:
    def __init__(self, repository: TagsRepository):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def create(self, tag_name: str):
        return await self.repository.create(tag_name)

    async def delete(self, tag_id: int):
        return await self.repository.delete(tag_id)
