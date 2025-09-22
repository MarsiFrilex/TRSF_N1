from src.repositories.statuses_repository import StatusesRepository


class StatusesService:
    def __init__(self, repository: StatusesRepository):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def create(self, status_name: str):
        return await self.repository.create(status_name)

    async def delete(self, status_id: int):
        return await self.repository.delete(status_id)
