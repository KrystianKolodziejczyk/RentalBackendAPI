from abc import ABC, abstractmethod
from pathlib import Path


class IStorageEnsure(ABC):
    @abstractmethod
    def get_path(fileName: str) -> Path: ...
