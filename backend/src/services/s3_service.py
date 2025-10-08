import uuid

from io import BytesIO
from fastapi import UploadFile

from src.database.s3_connection import get_s3_client


class S3Service:
    BUCKET_NAME = "b06cf1d0-trsf"

    @staticmethod
    async def create_filename(file_ext: str) -> str:
        return f"{str(uuid.uuid4())}.{file_ext}"

    async def upload_file(self, file: UploadFile, file_ext: str) -> dict:
        # Определение ключа файла
        file_key = await self.create_filename(file_ext)

        async for s3_client in get_s3_client():
            # Перематываем поток файла, чтобы начать с начала
            file.file.seek(0)

            # Загружаем файл
            await s3_client.upload_fileobj(file.file, self.BUCKET_NAME, file_key)

            # Возвращаем метаданные
            return {
                "strict_url": f"https://s3.twcstorage.ru/{self.BUCKET_NAME}/{file_key}",
                "content_type": file.content_type,
                "size": getattr(file, "size", None),
            }