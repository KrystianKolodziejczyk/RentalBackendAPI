from abc import ABC, abstractmethod

from app.modules.inventory.domain.models.car import Car


class IInventoryRepositoryV3(ABC):
    @abstractmethod
    async def get_all_cars(self) -> list[Car]: ...

    @abstractmethod
    async def get_one_car(self, car_id: int) -> Car: ...

    @abstractmethod
    async def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    async def add_car(self, car: Car) -> int: ...

    @abstractmethod
    async def delete_car(self, car_id: int) -> int: ...

    @abstractmethod
    async def update_car(self, car_id: int, car: Car) -> int: ...
