from app.modules.inventory.domain.exceptions.inventory_exceptions import (
    CarNotFoundException,
)
from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.repositories.i_inventory_repository import (
    IInventoryRepository,
)
from app.modules.inventory.domain.services.i_inventory_service import (
    IInventoryService,
)
from app.modules.inventory.presentation.dto import CreateCarDTO, UpdateCarDTO


class InventoryService(IInventoryService):
    _inventory_repository: IInventoryRepository

    def __init__(self, inventory_repository: IInventoryRepository):
        self._inventory_repository = inventory_repository

    # Helper looks for car
    async def _get_car_and_check(self, car_id: int) -> Car:
        car: Car = await self._inventory_repository.get_car_by_id(car_id=car_id)
        if not car:
            raise CarNotFoundException(car_id=car_id)

        return car

    # Returns all cars
    async def get_all_cars(self) -> list[Car]:
        return await self._inventory_repository.get_all_cars()

    # Gets car by id
    async def get_car_by_id(self, car_id: int) -> Car:
        return await self._get_car_and_check(car_id=car_id)

    # Get all cars qty
    async def get_all_cars_qty(self) -> int:
        return await self._inventory_repository.get_all_cars_qty()

    # Adds new car
    async def add_car(self, create_car_dto: CreateCarDTO) -> int:
        new_id: int = await self._inventory_repository.add_car(
            car=Car.create(
                brand=create_car_dto.brand,
                model=create_car_dto.model,
                year=create_car_dto.year,
            )
        )

        return new_id

    # Deletes car
    async def delete_car(self, car_id: int) -> int:
        car: Car = await self._get_car_and_check(car_id=car_id)
        car.ensure_not_rented()

        await self._inventory_repository.delete_car(car_id=car_id)
        return car_id

    # Updates car
    async def update_car(self, car_id: int, update_car_dto: UpdateCarDTO) -> int:
        car: Car = await self._get_car_and_check(car_id=car_id)
        car.ensure_not_rented()
        car.update(
            brand=update_car_dto.brand,
            model=update_car_dto.model,
            year=update_car_dto.year,
        )
        await self._inventory_repository.update_car(car_id=car_id, car=car)
        return car_id

    # Gets available cars
    async def get_available_cars(self) -> list[Car]:
        return await self._inventory_repository.get_available_cars()

    # Returns car status
    async def check_car_status(self, car_id: int) -> str:
        car: Car = await self._get_car_and_check(car_id=car_id)
        return car.status.value

    async def change_car_status(self, car: Car) -> int:
        await self._inventory_repository.save_status(car=car)
