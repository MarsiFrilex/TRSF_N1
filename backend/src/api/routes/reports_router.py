import os
import tempfile
import pandas as pd

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from src.api.dependencies import get_defects_service
from src.services.defects_service import DefectsService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/{object_id}", summary="Скачать отчёт по id объекта")
async def get_report(
    object_id: int,
    defects_service: DefectsService = Depends(get_defects_service)
):
    defects = await defects_service.get_all_for_report(object_id=object_id)

    if defects and not isinstance(defects[0], dict):
        print('a', type(defects[0]))
        defects = [{key: str(value) for key, value in d.items()} for d in defects]

    df = pd.DataFrame(defects, columns=[
        "id",
        "title",
        "description",
        "tag",
        "status",
        "photo_url",
        "deadline",
        "registrator",
        "engineer",
        "created_at",
        "updated_at",
    ])

    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        file_path = tmp.name
        df.to_excel(file_path, index=False)

    filename = f"report_object_{object_id}.xlsx"
    headers = {
        "Content-Disposition": f"attachment; filename={filename}"
    }

    return FileResponse(
        path=file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=filename,
        headers=headers,
        background=None
    )