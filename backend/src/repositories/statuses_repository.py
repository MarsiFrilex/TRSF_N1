from sqlalchemy import insert, select, delete

from src.database.connection import async_session_maker
from src.database.models import Statuses


class StatusesRepository:

    @staticmethod
    async def get_all():
        async with async_session_maker() as session:
            result = await session.execute(select(Statuses))
            return result.scalars().all()

    @staticmethod
    async def create(status_name: str):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Statuses)
                .values(title=status_name)
                .returning(Statuses)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete(status_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Statuses)
                .where(Statuses.id == status_id)
                .returning(Statuses)
            )
            await session.commit()
            return result.scalar_one_or_none()
