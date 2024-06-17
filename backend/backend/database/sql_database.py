from backend.database.database import Database
from datetime import datetime

from backend.models.todo import Todo
from typing import List


class SQLDatabase(Database):
    def connect(self, **kwargs) -> bool:
        raise NotImplementedError

    def close(self) -> bool:
        raise NotImplementedError

    def is_connected(self) -> bool:
        raise NotImplementedError

    def __enter__(self, **kwargs) -> 'SQLDatabase':
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def get_todo_items(self) -> List[Todo]:
        raise NotImplementedError

    def get_todo_item(self, todo_id: str) -> Todo:
        raise NotImplementedError

    def update_todo(self, todo: Todo) -> Todo:
        raise NotImplementedError

    def mark_done_at(self, todo_id: str, done_at: datetime | None) -> Todo:
        raise NotImplementedError

    def add_todo(self, todo: Todo) -> Todo:
        raise NotImplementedError

    def remove_todo(self, todo_id: str) -> bool:
        raise NotImplementedError
