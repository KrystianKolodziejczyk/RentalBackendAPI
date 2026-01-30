from abc import ABC, abstractmethod

from app.modules.rental.domain.models.rental import Rental


class IRentalRepository(ABC):
    @abstractmethod
    async def get_rental_by_id(self, rental_id: int) -> Rental: ...

    @abstractmethod
    async def get_all_rentals(self) -> list[Rental]: ...

    @abstractmethod
    async def check_rental_id(self, car_id: int) -> int | None: ...

    @abstractmethod
    async def rent_car(self, rental: Rental) -> tuple[int | str, ...]: ...

    @abstractmethod
    async def return_car(self, rental: Rental) -> tuple[int | str, ...]: ...
