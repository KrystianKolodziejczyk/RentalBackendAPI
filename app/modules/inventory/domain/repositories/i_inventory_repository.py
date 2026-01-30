from abc import ABC, abstractmethod

from app.modules.inventory.domain.models.car import Car


class IInventoryRepository(ABC):
    @abstractmethod
    async def get_all_cars(self) -> list[Car]: ...

    @abstractmethod
    async def get_car_by_id(self, car_id: int) -> Car: ...

    @abstractmethod
    async def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    async def add_car(self, car: Car) -> None: ...

    @abstractmethod
    async def delete_car(self, car_id: int) -> None: ...

    @abstractmethod
    async def update_car(self, car: Car) -> None: ...

    @abstractmethod
    async def get_available_cars(self) -> list[Car]: ...

    @abstractmethod
    async def save_status(self, car: int) -> int: ...
