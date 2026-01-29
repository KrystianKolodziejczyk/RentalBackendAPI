from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.inventory.domain.exceptions.inventory_exceptions import (
    CarAlreadyRentedException,
)


class Car:
    id: int | None
    brand: str
    model: str
    year: int
    status: RentStatusEnum

    def __init__(
        self, id: int, brand: str, model: str, year: int, status: RentStatusEnum
    ) -> None:
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.status = status

    @classmethod
    def create(cls, brand: str, model: str, year: int) -> "Car":
        return cls(
            id=None,
            brand=brand,
            model=model,
            year=year,
            status=RentStatusEnum.AVAILABLE,
        )

    def ensure_not_rented(self) -> None:
        if self.status == RentStatusEnum.RENTED:
            raise CarAlreadyRentedException(self.id)

    def update(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
