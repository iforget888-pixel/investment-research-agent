from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field(
        default="postgresql+psycopg://research:research@localhost:5432/investment_research",
        alias="DATABASE_URL",
    )
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    object_storage_endpoint: str = Field(default="http://localhost:9000", alias="OBJECT_STORAGE_ENDPOINT")
    object_storage_bucket: str = Field(default="research-artifacts", alias="OBJECT_STORAGE_BUCKET")
    object_storage_access_key: str = Field(default="research", alias="OBJECT_STORAGE_ACCESS_KEY")
    object_storage_secret_key: str = Field(default="research-password", alias="OBJECT_STORAGE_SECRET_KEY")
    cors_origins: str = Field(default="http://localhost:5173", alias="CORS_ORIGINS")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
