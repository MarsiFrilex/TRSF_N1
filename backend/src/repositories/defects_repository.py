from sqlalchemy import insert, select, update, delete, and_, func
from sqlalchemy.orm import aliased

from src.schemas.defects_schemas import CreateDefectSchema, UpdateDefectSchema
from src.database.pg_connection import async_session_maker
from src.database.models import Defects, Tags, Statuses, Users


class DefectsRepository:

    @staticmethod
    async def get_all(object_id: int = None, status_id: int = None):
        registrator = aliased(Users)
        engineer = aliased(Users)

        async with async_session_maker() as session:
            query = (
                select(
                    Defects.id.label("id"),
                    Defects.title.label("title"),
                    Defects.description.label("description"),
                    Tags.title.label("tag"),
                    Statuses.title.label("status"),
                    Defects.photo_url.label("photo_url"),
                    func.to_char(Defects.deadline, "YYYY-MM-DD").label("deadline"),
                    registrator.user_name.label("registrator"),
                    engineer.user_name.label("engineer"),
                )
                .select_from(Defects)
                .join(Tags, Tags.id == Defects.tag_id)
                .join(Statuses, Statuses.id == Defects.status_id)
                .join(registrator, registrator.id == Defects.registrator_id)
                .join(engineer, engineer.id == Defects.engineer_id)
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
    async def get_all_for_report(object_id: int):
        registrator = aliased(Users)
        engineer = aliased(Users)

        async with async_session_maker() as session:
            query = (
                select(
                    Defects.id.label("id"),
                    Defects.title.label("title"),
                    Defects.description.label("description"),
                    Tags.title.label("tag"),
                    Statuses.title.label("status"),
                    Defects.photo_url.label("photo_url"),
                    func.to_char(Defects.deadline, "YYYY-MM-DD").label("deadline"),
                    registrator.user_name.label("registrator"),
                    engineer.user_name.label("engineer"),
                    Defects.created_at.label("created_at"),
                    Defects.updated_at.label("updated_at"),
                )
                .select_from(Defects)
                .join(Tags, Tags.id == Defects.tag_id)
                .join(Statuses, Statuses.id == Defects.status_id)
                .join(registrator, registrator.id == Defects.registrator_id)
                .join(engineer, engineer.id == Defects.engineer_id)
            )

            query = query.where(Defects.object_id == object_id)
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
                .values(**defect.model_dump(exclude_none=True, exclude_defaults=True))
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
