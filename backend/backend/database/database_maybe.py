# import json
# from datetime import datetime
# from pathlib import Path
#
# from backend.database.database_adapter import DatabaseAdapter, ResourceAlreadyExists, ResourceNotFound
# from backend.models.todo import Todo
# from typing import List, Dict
#
#
# class Database:
#     def __init__(self, adapter):
#         self.db = adapter()
#
#     def connect(self, **kwargs) -> bool:
#         self.db.connect(**kwargs)
#
#         return True
#
#     def close(self) -> bool:
#         self.db.close()
#         return True
#
#     def is_connected(self) -> bool:
#         return self.db.is_connected()
#
#     def __enter__(self, **kwargs) -> 'Database':
#         self.connect(**kwargs)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#
#     def get_todo_items(self) -> List[Todo]:
#         return self.db.get_todo_items()
#
#     def get_todo_item(self, todo_id: str) -> Todo:
#         return self.db.get_todo_item(todo_id)
#
#     def update_todo(self, todo: Todo) -> Todo:
#         return self.db.update_todo(todo)
#
#     def mark_done_at(self, todo_id: str, done_at: datetime | None) -> Todo:
#         return self.db.mark_done_at(todo_id, done_at)
#
#     def add_todo(self, todo: Todo) -> Todo:
#         return self.db.add_todo(todo)
#
#     def remove_todo(self, todo_id: str) -> bool:
#         return self.db.remove_todo(todo_id)
