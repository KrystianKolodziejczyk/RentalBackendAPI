from abc import ABC, abstractmethod

from app.modules.rental.domain.models.rental import Rental


class IRentalRepository(ABC):
    @abstractmethod
    async def get_rental_by_id(self, rental_id: int) -> Rental | None: ...

    @abstractmethod
    async def get_all_rentals(self) -> list[Rental]: ...

    @abstractmethod
    async def rent_car(self, rental: Rental) -> int: ...

    @abstractmethod
    async def return_car(self, rental: Rental) -> int: ...

    @abstractmethod
    async def get_active_rentals(self) -> list[Rental] | None: ...
