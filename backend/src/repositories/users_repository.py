from sqlalchemy import insert, select, update, delete

from src.database.connection import async_session_maker
from src.database.models import Users, Roles
from src.schemas.user_schemas import InsertUserSchema, UpdateUserSchema


class UsersRepository:

    @staticmethod
    async def get(user_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Users)
                .join(Roles, Roles.id == Users.role_id)
                .where(Users.id == user_id)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def get_by_email(email: str):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Users)
                .join(Roles, Roles.id == Users.role_id)
                .where(Users.email == email)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def create(user: InsertUserSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                insert(Users)
                .values(**user.model_dump())
                .returning(Users.id)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def update(user_id: int, user: UpdateUserSchema):
        async with async_session_maker() as session:
            result = await session.execute(
                update(Users)
                .values(**user.model_dump(exclude_none=True))
                .where(Users.id == user_id)
                .returning(Users)
            )
            await session.commit()
            return result.scalar_one_or_none()

    @staticmethod
    async def delete(user_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Users)
                .where(Users.id == user_id)
                .returning(Users)
            )
            await session.commit()
            return result.scalar_one_or_none()