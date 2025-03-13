from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str = "auth_db"
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE: int = 30  # minutes

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')


@lru_cache
def get_settings() -> Settings:
    return Settings()