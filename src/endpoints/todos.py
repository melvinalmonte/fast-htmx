import os
import uuid

from fastapi import APIRouter
from fastapi import Request, Response
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src import config
from src.common.logger import logger
from src.database.db import SessionLocal
from src.models.todo import get_all_todo_items

router = APIRouter()
app_config = config.get_config()

templates = Jinja2Templates(directory=app_config.TEMPLATES_DIR)


def setup_db():
    logger.info('Setting up database...')
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/', response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(setup_db)):
    session_key = request.cookies.get("session_key", uuid.uuid4().hex)
    todos = get_all_todo_items(db, session_key)
    context = {
        "request": request,
        "todos": todos,
        "title": "Home"
    }
    response = templates.TemplateResponse("home.html", context)
    response.set_cookie(key="session_key", value=session_key, expires=259200)  # 3 days
    return response
