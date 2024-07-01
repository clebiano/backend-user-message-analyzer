from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = Path(__file__).parents[1] / '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
