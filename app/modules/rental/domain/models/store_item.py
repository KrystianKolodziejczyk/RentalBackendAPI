from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum


# Store item class
class StoreItem:
    car: Car
    status: RentStatusEnum

    def __init__(self, car: Car, status: RentStatusEnum):
        self.car = car
        self.status = status
