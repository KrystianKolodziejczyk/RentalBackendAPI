from pathlib import Path
from app.shared.domain.services.storage_ensure.i_storage_ensure import IStorageEnsure


class StorageEnsure(IStorageEnsure):
    @staticmethod
    def get_path(file_name: str) -> Path:
        root = Path.cwd().resolve()
        database_dir = root / "database"
        json_file_path = database_dir / file_name

        if not json_file_path.exists():
            database_dir.mkdir(parents=True, exist_ok=True)
            json_file_path.write_text(data="[]")

        return json_file_path
