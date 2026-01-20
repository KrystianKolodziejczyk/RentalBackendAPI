from abc import ABC, abstractmethod

from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.presentation.dto.create_car_dto import CreateCarDTO


class IInventoryService(ABC):
    @abstractmethod
    def get_all_cars(self) -> list[Car]: ...

    @abstractmethod
    def get_car_by_id(self, car_id: int) -> Car: ...

    @abstractmethod
    def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    def add_car(self, create_car_dto: CreateCarDTO) -> int: ...

    @abstractmethod
    def delete_car(self, car_id: int) -> int: ...

    @abstractmethod
    def update_car(self, car_id: int) -> int: ...

    @abstractmethod
    def get_available_cars(self) -> list[Car]: ...

    @abstractmethod
    def check_car_status(self, car_id: int) -> RentStatusEnum: ...

    @abstractmethod
    def rent_car(self, car_id: int) -> RentStatusEnum: ...

    @abstractmethod
    def return_car(self, car_id: int) -> RentStatusEnum: ...
