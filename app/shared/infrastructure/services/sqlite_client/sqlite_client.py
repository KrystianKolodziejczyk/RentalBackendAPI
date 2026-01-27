from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, AsyncIterator

import aiosqlite

from app.shared.domain.services.i_sqlite_client.i_sqlite_client import ISqliteClient


class SqliteClient(ISqliteClient):
    _path: Path

    def __init__(self, path: Path):
        self._path = path

    @asynccontextmanager
    async def _get_connection(self) -> AsyncIterator[aiosqlite.Connection]:
        async with aiosqlite.connect(database=self._path) as conn:
            conn.row_factory = aiosqlite.Row
            yield conn

    async def fetch_one(
        self, query: str, params: tuple | dict | None = None
    ) -> dict[str, Any]:
        async with self._get_connection() as conn:
            cursor = await conn.execute(query, params)
            row = await cursor.fetchone()

            if row is None:
                return None
            return dict(row)

    async def fetch_all(
        self, query: str, params: tuple | dict | None = None
    ) -> list[dict]:
        async with self._get_connection() as conn:
            cursor = await conn.execute(query, params)
            rows = await cursor.fetchall()

            if rows is None:
                return None
            return [dict(row) for row in rows]

    async def execute(self, query: str, params: tuple | dict | None = None) -> int:
        async with self._get_connection() as conn:
            cursor = await conn.execute(query, params)
            await conn.commit()

            if cursor.lastrowid:
                return cursor.lastrowid

            return cursor.rowcount

    async def execute_many(
        self, query: str, params_list: list[tuple | dict] | None = None
    ) -> int:
        async with self._get_connection() as conn:
            cursor = await conn.executemany(query, params_list)
            await conn.commit()

            return cursor.rowcount
