from abc import ABC, abstractmethod

from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.store_item import StoreItem


class IRentalService(ABC):
    @abstractmethod
    def get_all_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def get_car_by_id(self, car_id: int) -> StoreItem: ...

    @abstractmethod
    def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    def add_car(self, createCarDTO) -> None: ...

    @abstractmethod
    def delete_car(self, car_id: int) -> None: ...

    @abstractmethod
    def update_car(self, car_id: int) -> int: ...

    @abstractmethod
    def get_available_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def check_car_availability(self, id: int) -> str: ...

    @abstractmethod
    def rent_car(self, id: int) -> RentStatusEnum: ...

    @abstractmethod
    def return_car(self, id: int) -> RentStatusEnum: ...
