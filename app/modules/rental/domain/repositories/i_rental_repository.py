from abc import ABC, abstractmethod
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.models.store_item import StoreItem


class IRentalRepository(ABC):
    @abstractmethod
    def get_all_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def get_car_by_id(self, car_id: int) -> StoreItem: ...

    @abstractmethod
    def get_all_cars_qty(self) -> int: ...

    @abstractmethod
    def add_car(self, car: Car, newId: int) -> None: ...

    @abstractmethod
    def delete_car(self, car_id: int) -> bool: ...

    @abstractmethod
    def update_car(self, car_id: int, car: Car) -> int: ...

    @abstractmethod
    def get_available_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def find_available_car(self, car_id: int) -> str: ...
