from sqlalchemy import insert, select, update, delete

from src.schemas.objects_schemas import CreateObjectSchema, UpdateObjectSchema
from src.database.pg_connection import async_session_maker
from src.database.models import Objects


class ObjectsRepository:

    @staticmethod
    async def get_all():
        async with async_session_maker() as session:
            result = await session.execute(select(Objects))
            return result.scalars().all()

    @staticmethod
    async def get(object_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Objects).where(Objects.id == object_id)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def create(obj: CreateObjectSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Objects)
                .values(**obj.model_dump())
                .returning(Objects.id)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def update(object_id: int, obj: UpdateObjectSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                update(Objects)
                .values(**obj.model_dump(exclude_none=True))
                .where(Objects.id == object_id)
                .returning(Objects)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete(object_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Objects)
                .where(Objects.id == object_id)
                .returning(Objects)
            )
            await session.commit()
            return result.scalar_one_or_none()
