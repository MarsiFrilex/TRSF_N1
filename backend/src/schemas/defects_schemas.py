from datetime import datetime

from pydantic import BaseModel


class CreateDefectSchema(BaseModel):
    title: str
    description: str
    object_id: int
    tag_id: int
    registrator_id: int
    engineer_id: int
    status_id: int
    deadline: datetime


class UpdateDefectSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    object_id: int | None = None
    tag_id: int | None = None
    registrator_id: int | None = None
    engineer_id: int | None = None
    status_id: int | None = None
    deadline: datetime | None = None