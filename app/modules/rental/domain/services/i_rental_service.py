from abc import ABC, abstractmethod

from app.modules.rental.domain.models.rental import Rental
from app.modules.rental.presentation.dto.rent_car_dto import RentCarDto


class IRentalService(ABC):
    @abstractmethod
    async def get_rental_by_id(self, rental_id: int) -> Rental | None: ...

    @abstractmethod
    async def get_all_rentals(self) -> list[Rental]: ...

    @abstractmethod
    async def rent_car(self, rent_car_dto: RentCarDto) -> int: ...

    @abstractmethod
    async def return_car(self, rental_id: int) -> int: ...

    @abstractmethod
    async def get_active_rentals(self) -> list[Rental] | None: ...
