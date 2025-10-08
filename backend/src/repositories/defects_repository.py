from sqlalchemy import insert, select, update, delete, and_

from src.schemas.defects_schemas import CreateDefectSchema, UpdateDefectSchema
from src.database.pg_connection import async_session_maker
from src.database.models import Defects, Tags, Statuses


class DefectsRepository:

    @staticmethod
    async def get_all(object_id: int = None, status_id: int = None):
        async with async_session_maker() as session:
            query = (
                select(
                    Defects.id.label("id"),
                    Defects.title.label("title"),
                    Defects.description.label("description"),
                    Tags.title.label("tag"),
                    Statuses.title.label("status")
                )
                .select_from(Defects)
                .join(Tags, Tags.id == Defects.tag_id)
                .join(Statuses, Statuses.id == Defects.status_id)
            )

            filters = []
            if object_id is not None:
                filters.append(Defects.object_id == object_id)
            if status_id is not None:
                filters.append(Defects.status_id == status_id)

            if filters:
                query = query.where(and_(*filters))

            result = await session.execute(query)
            return result.mappings().all()

    @staticmethod
    async def get(defect_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Defects).where(Defects.id == defect_id)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def create(defect: CreateDefectSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Defects)
                .values(**defect.model_dump())
                .returning(Defects.id)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def update(defect_id: int, defect: UpdateDefectSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                update(Defects)
                .values(**defect.model_dump(exclude_none=True))
                .where(Defects.id == defect_id)
                .returning(Defects)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete(defect_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Defects)
                .where(Defects.id == defect_id)
                .returning(Defects)
            )
            await session.commit()
            return result.scalar_one_or_none()
