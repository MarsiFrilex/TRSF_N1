from sqlalchemy import insert, select, delete

from src.database.connection import async_session_maker
from src.database.models import Roles


class RolesRepository:

    @staticmethod
    async def get_all():
        async with async_session_maker() as session:
            result = await session.execute(select(Roles))
            return result.scalars().all()

    @staticmethod
    async def create(role_name: str):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Roles)
                .values(title=role_name)
                .returning(Roles)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete(role_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Roles)
                .where(Roles.id == role_id)
                .returning(Roles)
            )
            await session.commit()
            return result.scalar_one_or_none()
