import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_TITLE: str = 'Fast ToDos'
    APP_VERSION: str = '0.0.0'
    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 5001
    DOCS_URL: str = '/api/docs'
    OPEN_API_URL: str = '/api/openapi.json'
    TEMPLATES_DIR: str = os.path.join(os.path.dirname(__file__), 'templates')
    BACKEND_CORS_ORIGIN: list = ["*"]


@lru_cache()
def get_config():
    config = Config()
    return config
