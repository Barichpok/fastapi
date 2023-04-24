import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '..', '..', '.env')


settings = Settings()
