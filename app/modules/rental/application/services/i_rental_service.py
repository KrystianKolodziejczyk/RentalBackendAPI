from abc import ABC, abstractmethod
from datetime import datetime

from app.modules.rental.domain.models.rental import Rental


class IRentalService(ABC):
    @abstractmethod
    async def get_rental_by_id(self, rental_id: int) -> Rental | None: ...

    @abstractmethod
    async def get_all_rentals(self) -> list[Rental]: ...

    @abstractmethod
    async def check_rental_id(self, car_id: int) -> int | None: ...

    @abstractmethod
    async def rent_car(self, customer_id: int, car_id: int) -> int: ...

    @abstractmethod
    async def return_car(self, car_id: int, return_timestamp: datetime) -> int: ...
