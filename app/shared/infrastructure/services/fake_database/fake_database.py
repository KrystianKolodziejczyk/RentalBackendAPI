import json
from pathlib import Path

from app.shared.domain.services.i_fake_database.i_fake_database import IFakeDatabase


class FakeDatabse(IFakeDatabase):
    @staticmethod
    def get_json_list(path: Path) -> list[dict]:
        with open(path, mode="r", encoding="utf-8", newline=None) as f:
            return json.load(f)

    @staticmethod
    def save_json_list(path: Path, python_data: list[dict]) -> None:
        with open(path, mode="w", encoding="utf-8", newline=None) as f:
            json.dump(python_data, f)
