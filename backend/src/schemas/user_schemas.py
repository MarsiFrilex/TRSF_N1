from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    email: str
    user_name: str
    password: str
    role_id: int


class UpdateUserSchema(BaseModel):
    email: str | None = None
    user_name: str | None = None
    password: str | None = None
    role_id: int | None = None


class InsertUserSchema(BaseModel):
    email: str
    user_name: str
    hashed_password: str
    role_id: int