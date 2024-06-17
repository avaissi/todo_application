from abc import ABC, abstractmethod
from datetime import datetime

from backend.models.todo import Todo
from typing import List


class ResourceAlreadyExists(ValueError):
    pass


class ResourceNotFound(ValueError):
    pass


class Database(ABC):
    @abstractmethod
    def connect(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def close(self) -> bool:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def __enter__(self, **kwargs) -> 'Database':
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def get_todo_items(self) -> List[Todo]:
        pass

    @abstractmethod
    def get_todo_item(self, todo_id: str) -> Todo:
        pass

    @abstractmethod
    def update_todo(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    def mark_done_at(self, todo_id: str, done_at: datetime | None) -> Todo:
        pass

    @abstractmethod
    def add_todo(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    def remove_todo(self, todo_id: str) -> bool:
        pass
