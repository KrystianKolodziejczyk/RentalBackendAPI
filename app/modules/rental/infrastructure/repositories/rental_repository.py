from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository


# Storehouse Class
class RentalRepository(IRentalRepository):
    ownedCars: list[StoreItem]
    generalId: int = 0

    def __init__(self) -> None:
        self.ownedCars = []
        self.generalId += 1

    # Returns list of all instances
    def get_all_cars(self) -> list[StoreItem]:
        return self.ownedCars

    # Returns store's item instance
    def get_car_by_id(self, item_id: int) -> StoreItem:
        for item in self.ownedCars:
            if item.car.id == item_id:
                return item

    def add_car(self, car: Car) -> None:
        self.ownedCars.append(StoreItem(car=car, status=RentStatusEnum.AVAILABLE))

    def delete_car(self, car_id):
        for item in self.ownedCars:
            if item.car.id == car_id:
                self.ownedCars.remove(item)
                return True

        return False

    def get_available_cars(self) -> list[StoreItem]:
        return [
            item for item in self.ownedCars if item.status == RentStatusEnum.AVAILABLE
        ]

    def find_availabile_car_by_id(self, item_id) -> StoreItem:
        for item in self.ownedCars:
            if item_id == item.car.id and item.status == RentStatusEnum.AVAILABLE:
                return item

    def get_all_cars_qty(self):
        return len(self.ownedCars)
