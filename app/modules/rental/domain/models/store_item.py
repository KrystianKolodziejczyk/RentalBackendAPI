from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum


# Store item class
class StoreItem:
    car: Car
    status: RentStatusEnum

    def __init__(self, car: Car, status: RentStatusEnum):
        self.car = car
        self.status = status


firstCar: StoreItem = StoreItem(
    car=Car(brand="BMW", model="M4", year=2022), status=RentStatusEnum.AVAILABLE
)

print(firstCar.car.model)
