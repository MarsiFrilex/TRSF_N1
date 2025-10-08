from fastapi import Depends, APIRouter, UploadFile, File

from src.api.dependencies import get_s3_service
from src.services.s3_service import S3Service

router = APIRouter(
    prefix="/cloud",
    tags=["S3 Cloud"],
)


@router.post("")
async def upload_photo(
        file: UploadFile = File(...),
        s3: S3Service = Depends(get_s3_service),
):
    return await s3.upload_file(file, file.filename.split(".")[-1])