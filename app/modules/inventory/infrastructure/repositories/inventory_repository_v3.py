from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.repositories.i_inventory_repository_v3 import (
    IInventoryRepositoryV3,
)
from app.modules.inventory.infrastructure.mappers.car_mapper import CarMapper
from app.shared.domain.services.i_sqlite_client.i_sqlite_client import ISqliteClient


class InventoryRepositoryV3(IInventoryRepositoryV3):
    _db_client: ISqliteClient

    def __init__(self, db_client: ISqliteClient) -> None:
        self._db_client = db_client

    # Returns one car from DB
    async def get_one_car(self, car_id: int) -> Car:
        query: str = "SELECT * FROM cars WHERE id = ?"
        car_dict: dict = await self._db_client.fetch_one(query=query, params=(car_id,))
        return CarMapper.dict_to_car(car_dict=car_dict)

    # Returns all cars from DB
    async def get_all_cars(self) -> list[Car]:
        query: str = "SELECT * FROM cars"
        list_car_dict: list[dict] = await self._db_client.fetch_all(query=query)
        return [CarMapper.dict_to_car(car_dict) for car_dict in list_car_dict]

    # Returns all cars qty from DB
    async def get_all_cars_qty(self) -> int:
        query: str = "SELECT COUNT(id) FROM cars"
        cars_qty: dict = await self._db_client.fetch_one(query=query)
        return int(cars_qty.values())

    # Adds new car to DB
    async def add_car(self, car: Car) -> int:
        query: str = "INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)"
        car_dict: dict = CarMapper.car_to_dict(car=car)
        modified_rows: int = await self._db_client.execute(
            query=query, params=(car_dict["brand"], car_dict["model"], car_dict["year"])
        )

        return modified_rows

    # Deletes car from DB
    async def delete_car(self, car_id: int) -> int:
        query: str = "DELETE FROM cars WHERE id = ?"
        modified_rows: int = await self._db_client.execute(query=query, params=(car_id,))

        return modified_rows

    # Updates car in DB
    async def update_car(self, car_id: int, car: Car) -> int:
        query: str = "UPDATE cars SET brand = ?, model = ?, year = ? WHERE id = ?"
        car_dict: dict = CarMapper.car_to_dict(car=car)
        modified_rows: int = await self._db_client.execute(
            query=query, params=(car_dict["brand"], car_dict["model"], car_dict["year"], car_id)
        )

        return modified_rows
