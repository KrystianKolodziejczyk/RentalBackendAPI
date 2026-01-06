from abc import ABC, abstractmethod

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
    def get_available_cars(self) -> list[StoreItem]: ...

    @abstractmethod
    def find_availabile_car_by_id(self, id: int) -> str: ...

    @abstractmethod
    def rent_car(self, id: int) -> None: ...

    @abstractmethod
    def return_car(self, id: int) -> None: ...
