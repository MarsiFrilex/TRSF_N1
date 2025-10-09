from src.repositories.roles_repository import RolesRepository


class RolesService:
    def __init__(self, repository: RolesRepository):
        self.repository = repository

    async def get_all(self):
        return await self.repository.get_all()

    async def get_manager(self):
        return await self.repository.get_manager()

    async def create(self, role_name: str):
        return await self.repository.create(role_name)

    async def delete(self, role_id: int):
        return await self.repository.delete(role_id)