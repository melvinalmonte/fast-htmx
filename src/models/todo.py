from src.database.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    session_key = Column(String)


def add_todo_item(db: Session, content, session_key):
    todo = Todo(
        content=content,
        session_key=session_key
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo_item(db: Session, todo_id):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo_item(db: Session, todo_id, content):
    todo = get_todo_item(db, todo_id)
    todo.content = content
    db.commit()
    db.refresh(todo)
    return todo


def get_all_todo_items(db: Session, session_key: str, skip: int = 0, limit: int = 100):
    return db.query(Todo).filter(Todo.session_key == session_key).offset(skip).limit(limit).all()


def delete_todo_item(db: Session, todo_id: int):
    todo = get_todo_item(db, todo_id)
    db.delete(todo)
    db.commit()
    return todo
