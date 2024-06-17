from pydantic_settings import BaseSettings
from pathlib import Path


def get_json_file_path():
    return Path.home() / "json_db" / "todo.json"


class Settings(BaseSettings):
    json_file_path: str = str(get_json_file_path())
