from datetime import datetime

from pydantic import BaseModel


class CreateDefectSchema(BaseModel):
    title: str
    description: str
    photo_url: str
    object_id: int
    tag_id: int
    registrator_id: int
    engineer_id: int
    status_id: int
    deadline: datetime | str = ""


class UpdateDefectSchema(BaseModel):
    title: str | None = ""
    description: str | None = ""
    object_id: int | str | None = ""
    tag_id: int | str | None = ""
    registrator_id: int | str | None = ""
    engineer_id: int | str | None = ""
    status_id: int | str | None = ""
    deadline: datetime | None = ""