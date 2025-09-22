from sqlalchemy import insert, select, delete

from src.database.connection import async_session_maker
from src.database.models import Tags


class TagsRepository:

    @staticmethod
    async def get_all():
        async with async_session_maker() as session:
            result = await session.execute(select(Tags))
            return result.scalars().all()

    @staticmethod
    async def create(tag_name: str):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Tags)
                .values(title=tag_name)
                .returning(Tags)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete(tag_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Tags)
                .where(Tags.id == tag_id)
                .returning(Tags)
            )
            await session.commit()
            return result.scalar_one_or_none()
