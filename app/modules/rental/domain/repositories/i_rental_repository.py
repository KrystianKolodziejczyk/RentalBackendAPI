from abc import ABC, abstractmethod

from app.modules.rental.domain.models.rental import Rental


class IRentalRepository(ABC):
    @abstractmethod
    async def get_rental_by_id(
        self, customer_id: int | None = None, car_id: int | None = None
    ) -> Rental: ...

    @abstractmethod
    async def get_all_rentals(self) -> list[Rental]: ...

    @abstractmethod
    async def rent_car(
        self, customer_id: int, car_id: int, start_date: str, planned_end_date: str
    ) -> tuple[int | str, ...]: ...

    @abstractmethod
    async def return_car(
        self, customer_id: int, car_id: int, actual_end_date: str
    ) -> tuple[int | str, ...]: ...
