from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_URL: str = ""

    SECRET_KEY: str = "string"
    ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(env_file='../.env')


config = Config()