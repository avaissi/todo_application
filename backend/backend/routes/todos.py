from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import Optional

from backend.models.todo import TodoModel, Todo
from backend.config.settings import Settings
from backend.database.json_database import JSONDatabase, ResourceNotFound, ResourceAlreadyExists

settings = Settings()

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)

todos = {
    "todo1": Todo("Todo content for 1", datetime.now(), todo_id="todo1"),
    "todo2": Todo("Todo content for 2", datetime(2013, 5, 15, 13), todo_id="todo2"),
}


@router.get("/")
async def read_todos():
    with JSONDatabase(settings.json_file_path) as db:
        items = db.get_todo_items()
    return items


@router.get("/{todo_id}")
async def read_todo(todo_id: str) -> TodoModel:
    try:
        with JSONDatabase(settings.json_file_path) as db:
            item = db.get_todo_item(todo_id)
    except ResourceNotFound:
        raise HTTPException(status_code=404, detail="Todo item not found")

    return TodoModel(id=item.id, content=item.content, created_at=item.created_at, done_at=item.done_at)


@router.post(
    "/",
    responses={403: {"description": "Forbidden"}}
)
async def add_todo(todo: TodoModel) -> TodoModel:
    try:
        with JSONDatabase(settings.json_file_path) as db:
            item = db.add_todo(Todo(todo.content, todo.created_at, done_at=todo.done_at, todo_id=todo.id))
    except ResourceAlreadyExists:
        raise HTTPException(status_code=403, detail="Todo item already exists")

    return TodoModel(id=item.id, content=item.content, created_at=item.created_at, done_at=item.done_at)


@router.put(
    "/",
    responses={404: {"description": "Not found"}},
)
async def update_todo(todo: TodoModel) -> TodoModel:
    try:
        with JSONDatabase(settings.json_file_path) as db:
            item = db.update_todo(Todo(todo.content, todo.created_at, done_at=todo.done_at, todo_id=todo.id))
    except ResourceNotFound:
        raise HTTPException(status_code=404, detail="Todo item not found")

    return TodoModel(id=item.id, content=item.content, created_at=item.created_at, done_at=item.done_at)


@router.put(
    "/{todo_id}",
    responses={404: {"description": "Not found"}},
)
async def mark_todo_done_at(todo_id: str, done_at: Optional[datetime] = None) -> TodoModel:
    try:
        with JSONDatabase(settings.json_file_path) as db:
            item = db.mark_done_at(todo_id, done_at)
    except ResourceNotFound:
        raise HTTPException(status_code=404, detail="Todo item not found")

    return TodoModel(id=item.id, content=item.content, created_at=item.created_at, done_at=item.done_at)


@router.delete(
    "/{todo_id}",
    responses={404: {"description": "Not found"}},
)
async def delete_todo(todo_id: str) -> bool:
    try:
        with JSONDatabase(settings.json_file_path) as db:
            success = db.remove_todo(todo_id)
    except ResourceNotFound:
        raise HTTPException(status_code=404, detail="Todo item not found")

    return success
