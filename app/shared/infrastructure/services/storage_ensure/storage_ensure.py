from pathlib import Path
from app.shared.domain.services.storage_ensure.i_storage_ensure import IStorageEnsure


class StorageEnsure(IStorageEnsure):
    @staticmethod
    def get_path(file_name: str) -> Path:
        root = Path.cwd().resolve()
        database_dir = root / "database"
        databae_db = database_dir / file_name

        if not databae_db.exists():
            database_dir.mkdir(parents=True, exist_ok=True)
            databae_db.touch(exist_ok=True)

        return databae_db
