import json
from datetime import datetime
from pathlib import Path

from backend.database.database import Database, ResourceAlreadyExists, ResourceNotFound
from backend.models.todo import Todo, TodoJSONEncoder, todo_decoder
from typing import List, Dict, Optional, Union


class JSONDatabase(Database):
    file_path: Path | None = None
    db_content: Dict[str, Todo] = {}

    def __init__(self, path: Optional[Union[Path, str]] = None):
        self.file_path = Path(path)

    def connect(self, **kwargs) -> bool:
        if self.file_path is None and "path" not in kwargs:
            raise KeyError("Missing path to JSON file.")
        file_path = self.file_path or Path(kwargs["path"])
        self.file_path = file_path
        if not self.file_path.exists():
            self._write_to_file()
        self._read_from_file()

        return True

    def close(self) -> bool:
        if not self.file_path.exists():
            raise BrokenPipeError("Unable to close database file.")
        self._write_to_file()
        self.file_path = None
        return True

    def is_connected(self) -> bool:
        return self.file_path is not None and self.file_path.exists()

    def __enter__(self) -> 'JSONDatabase':
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_todo_items(self) -> List[Todo]:
        self._read_from_file()
        return [item for item in self.db_content.values()]

    def get_todo_item(self, todo_id: str) -> Todo:
        self._read_from_file()
        if todo_id not in self.db_content:
            raise ResourceNotFound(f"${todo_id} not found.")
        return self.db_content[todo_id]

    def update_todo(self, todo: Todo) -> Todo:
        self._read_from_file()
        if todo.id not in self.db_content:
            raise ResourceNotFound(f"${todo.id} not found.")
        item = Todo(todo.content, todo.created_at, done_at=todo.done_at, todo_id=todo.id)
        self.db_content[todo.id] = item
        self._write_to_file()
        return item

    def mark_done_at(self, todo_id: str, done_at: datetime | None) -> Todo:
        self._read_from_file()
        if todo_id not in self.db_content:
            raise ResourceNotFound(f"${todo_id} not found.")
        item = self.db_content[todo_id]
        modified_item = Todo(item.content, item.created_at, done_at=done_at, todo_id=item.id)
        self.db_content[todo_id] = modified_item
        self._write_to_file()
        return modified_item

    def add_todo(self, todo: Todo) -> Todo:
        self._read_from_file()
        if todo.id in self.db_content:
            raise ResourceAlreadyExists(f"${todo.id} already exists.")
        item = Todo(todo.content, todo.created_at, done_at=todo.done_at, todo_id=todo.id)
        self.db_content[item.id] = item
        self._write_to_file()
        return item

    def remove_todo(self, todo_id: str) -> bool:
        self._read_from_file()
        if todo_id not in self.db_content:
            raise ResourceNotFound(f"${todo_id} not found.")
        del self.db_content[todo_id]
        self._write_to_file()
        return True

    def _write_to_file(self):
        if not self.file_path.parent.exists():
            self.file_path.parent.mkdir(parents=True)
        with open(str(self.file_path), "w") as file:
            json_content = json.dumps(self.db_content, cls=TodoJSONEncoder)
            if json_content:
                file.write(json_content)

    def _read_from_file(self):
        with open(str(self.file_path), "r") as file:
            json_content = json.load(file, object_hook=todo_decoder)
            self.db_content = json_content
