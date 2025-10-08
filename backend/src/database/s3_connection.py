import aioboto3
from botocore.config import Config

from config import config

async def get_s3_client():
    session = aioboto3.Session()
    async with session.client(
        "s3",
        endpoint_url=config.S3_ENDPOINT,
        region_name=config.S3_REGION,
        aws_access_key_id=config.S3_ACCESS_KEY,
        aws_secret_access_key=config.S3_SECRET_KEY,
        config=Config(signature_version="s3v4"),
    ) as client:
        yield client