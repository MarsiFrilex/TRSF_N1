from pydantic import BaseModel


class CreateObjectSchema(BaseModel):
    address: str
    description: str


class UpdateObjectSchema(BaseModel):
    address: str | None = None
    description: str | None = None