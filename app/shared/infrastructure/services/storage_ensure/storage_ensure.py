from pathlib import Path
from app.shared.domain.services.storage_ensure.i_storage_ensure import IStorageEnsure
from app.shared.infrastructure.services.fake_database.fake_database import FakeDatabse


class StorageEnsure(IStorageEnsure):
    @staticmethod
    def get_path(fileName: str) -> Path:
        cwdPath = Path.cwd().resolve()
        databaseDir = cwdPath / "database"
        jsonFilePath = databaseDir / fileName

        if not jsonFilePath.exists():
            databaseDir.mkdir(parents=True, exist_ok=True)
            jsonFilePath.touch(exist_ok=True)

            FakeDatabse.save_json_list(path=jsonFilePath, pythonData=[])

        return jsonFilePath
