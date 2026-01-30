from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.repositories.i_inventory_repository import (
    IInventoryRepository,
)
from app.modules.inventory.infrastructure.mappers.car_mapper import CarMapper
from app.shared.domain.services.i_sqlite_client.i_sqlite_client import ISqliteClient


class InventoryRepository(IInventoryRepository):
    _db_client: ISqliteClient

    def __init__(self, db_client: ISqliteClient) -> None:
        self._db_client = db_client

    # Returns one car from DB
    async def get_car_by_id(self, car_id: int) -> Car:
        query: str = "SELECT * FROM cars WHERE id = ?"
        car_dict: dict = await self._db_client.fetch_one(query=query, params=(car_id,))
        if not car_dict:
            return None

        return CarMapper.dict_to_car(car_dict=car_dict)

    # Returns all cars from DB
    async def get_all_cars(self) -> list[Car]:
        query: str = "SELECT * FROM cars"
        list_car_dict: list[dict] = await self._db_client.fetch_all(query=query)
        return [CarMapper.dict_to_car(car_dict) for car_dict in list_car_dict]

    # Returns all cars qty from DB
    async def get_all_cars_qty(self) -> int:
        query: str = "SELECT COUNT(id) as cars_qty FROM cars"
        cars_qty: dict = await self._db_client.fetch_one(query=query)

        return cars_qty["cars_qty"]

    # Adds new car to DB
    async def add_car(self, car: Car) -> int:
        query: str = "INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)"
        car_dict: dict = CarMapper.car_to_dict(car=car)
        new_id: int = await self._db_client.execute(
            query=query, params=(car_dict["brand"], car_dict["model"], car_dict["year"])
        )

        return new_id

    # Deletes car from DB
    async def delete_car(self, car_id: int) -> None:
        query: str = "DELETE FROM cars WHERE id = ?"
        await self._db_client.execute(query=query, params=(car_id,))

    # Updates car in DB
    async def update_car(self, car: Car) -> None:
        car_dict: dict = CarMapper.car_to_dict(car=car)
        query: str = """
        UPDATE cars
        SET brand = ?,
        model = ?,
        year = ?
        WHERE id = ?
        """

        await self._db_client.execute(
            query=query,
            params=(
                car_dict["brand"],
                car_dict["model"],
                car_dict["year"],
                car_dict["id"],
            ),
        )

    async def get_available_cars(self) -> list[Car]:
        query: str = "SELECT * FROM cars WHERE status = 'available'"
        list_car_dict: list[dict] = await self._db_client.fetch_all(query=query)
        return [CarMapper.dict_to_car(car_dict) for car_dict in list_car_dict]

    async def save_status(self, car: Car) -> int:
        car_dict: dict = CarMapper.car_to_dict(car=car)
        query: str = """
        UPDATE cars
        SET status = ?
        WHERE id = ?
        """

        await self._db_client.execute(
            query=query, params=(car_dict["status"], car_dict["id"])
        )
        return car_dict["id"]
