from json import JSONEncoder
from typing import Optional, Any, Union
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4


class Todo:
    id: str
    content: str
    created_at: datetime
    done_at: Optional[datetime]

    def __init__(self, content: str, created_at: Union[datetime, str], *,
                 done_at: Optional[Union[datetime, str]] = None,
                 todo_id: Optional[str] = None):
        self.id = todo_id or str(uuid4())
        self.content = content
        self.created_at = created_at if isinstance(created_at, datetime) else datetime.fromisoformat(created_at)
        if done_at is None:
            self.done_at = None
        else:
            self.done_at = done_at if isinstance(done_at, datetime) else datetime.fromisoformat(done_at)


class TodoModel(BaseModel):
    id: Optional[str]
    content: str
    created_at: datetime
    done_at: Optional[datetime]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "261ec91b-9c05-4854-afda-1baff7a8436e",
                "content": "Todo item content",
                "created_at": datetime(2024, 6, 15, 14, 0, 0).isoformat(),
                "done_at": datetime(2024, 6, 15, 16, 0, 0).isoformat(),
            }
        }


class TodoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Todo):
            return {
                "id": obj.id,
                "content": obj.content,
                "created_at": obj.created_at.isoformat() if obj.created_at else None,
                "done_at": obj.done_at.isoformat() if obj.done_at else None,
            }
        return super().default(obj)


def todo_decoder(data: Any):
    if data and "content" in data:
        return Todo(data["content"], data["created_at"], done_at=data["done_at"], todo_id=data["id"])
    return data
