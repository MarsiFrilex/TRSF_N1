from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')


class Config(Settings):
    DB_URL: str = ""

    SECRET_KEY: str = ""
    ALGORITHM: str = ""

    S3_ENDPOINT: str = ""
    S3_REGION: str = ""
    S3_ACCESS_KEY: str = ""
    S3_SECRET_KEY: str = ""


config = Config()