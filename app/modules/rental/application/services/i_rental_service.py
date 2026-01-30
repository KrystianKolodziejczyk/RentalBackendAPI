from abc import ABC, abstractmethod

from app.modules.rental.domain.models.rental import Rental


class RentalService(ABC):
    @abstractmethod
    async def get_rental_by_id(self, rental_id: int) -> Rental: ...

    @abstractmethod
    async def get_all_rentals(self) -> list[Rental]: ...

    @abstractmethod
    async def rent_car(self, customer_id: int, car_id: int) -> int: ...

    @abstractmethod
    async def return_car(self, car_id: int) -> int: ...
