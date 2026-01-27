from abc import ABC, abstractmethod
from typing import Any


class ISqliteClient(ABC):
    @abstractmethod
    async def fetch_one(
        self, query: str, params: tuple | dict | None = None
    ) -> dict[str, Any]: ...

    @abstractmethod
    async def fetch_all(
        self, query: str, params: tuple | dict | None = None
    ) -> dict[str, Any]: ...

    @abstractmethod
    async def execute(self, query: str, params: tuple | dict | None = None) -> int: ...

    @abstractmethod
    async def execute_many(
        self, query: str, params_list: list[tuple | dict] | None = None
    ) -> int: ...
