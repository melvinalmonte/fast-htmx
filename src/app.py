from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src import config
from src.api import router
from src.common.logger import logger
from src.database.db import Base, engine

app_config = config.get_config()

Base.metadata.create_all(bind=engine)


def create_app():
    logger.info('Starting application...')
    app = FastAPI(
        title=app_config.APP_TITLE,
        version=app_config.APP_VERSION,
        docs_url=app_config.DOCS_URL,
        openapi_url=app_config.OPEN_API_URL,
        on_startup=[create_app],
    )
    app.include_router(router, prefix='/api')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_config.BACKEND_CORS_ORIGIN,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return app
