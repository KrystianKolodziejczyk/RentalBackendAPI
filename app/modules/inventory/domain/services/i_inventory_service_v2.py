from abc import ABC, abstractmethod

from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.presentation.dto.create_car_dto import CreateCarDTO


class IInventoryServiceV2(ABC):
    @abstractmethod
    async def get_all_cars(self) -> list[Car]: ...

    @abstractmethod
    async def get_car_by_id(self, car_id: int) -> Car: ...

    @abstractmethod
    async def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    async def add_car(self, create_car_dto: CreateCarDTO) -> int: ...

    @abstractmethod
    async def delete_car(self, car_id: int) -> int: ...

    @abstractmethod
    async def update_car(self, car_id: int) -> int: ...

    @abstractmethod
    async def get_available_cars(self) -> list[Car]: ...

    @abstractmethod
    async def check_car_status(self, car_id: int) -> str: ...
