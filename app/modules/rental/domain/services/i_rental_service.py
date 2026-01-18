from abc import ABC, abstractmethod

from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.presentation.dto.create_car_dto import CreateCarDTO


class IRentalService(ABC):
    @abstractmethod
    def get_all_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def get_store_item_by_id(self, car_id: int) -> StoreItem: ...

    @abstractmethod
    def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    def add_car(self, create_car_dto: CreateCarDTO) -> int: ...

    @abstractmethod
    def delete_car(self, car_id: int) -> None: ...

    @abstractmethod
    def update_car(self, car_id: int) -> int: ...

    @abstractmethod
    def get_available_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def check_car_status(self, car_id: int) -> str: ...

    @abstractmethod
    def rent_car(self, car_id: int) -> RentStatusEnum: ...

    @abstractmethod
    def return_car(self, car_id: int) -> RentStatusEnum: ...
