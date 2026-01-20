from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum


class Car:
    id: int
    brand: str
    model: str
    year: int
    status: RentStatusEnum

    def __init__(
        self,
        id: int,
        brand: str,
        model: str,
        year: int,
        status: RentStatusEnum = RentStatusEnum.AVAILABLE,
    ) -> None:
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.status = status
