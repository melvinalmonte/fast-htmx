from fastapi import APIRouter

from src.endpoints import healthcheck, todos

router = APIRouter()

router.include_router(healthcheck.router, tags=['healthcheck'])
router.include_router(todos.router, tags=['todos'])
