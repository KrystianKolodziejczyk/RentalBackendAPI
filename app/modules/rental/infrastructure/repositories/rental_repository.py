from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository


# Storehouse Class
class RentalRepository(IRentalRepository):
    ownedCars: list[StoreItem]
    generalId: int

    def __init__(self) -> None:
        self.ownedCars = []
        self.generalId = 0

    # Returns list of all instances
    def get_all_cars(self) -> list[StoreItem]:
        return self.ownedCars

    # Returns store's item instance
    def get_car_by_id(self, car_id: int) -> StoreItem:
        for item in self.ownedCars:
            if item.car.id == car_id:
                return item

    def get_all_cars_qty(self) -> int:
        return int(len(self.ownedCars))

    def add_car(self, createCarDTO: Car, newId: int) -> None:
        newCar: StoreItem = StoreItem(
            car=Car(
                id=newId,
                brand=createCarDTO.brand,
                model=createCarDTO.model,
                year=createCarDTO.year,
            ),
            status=RentStatusEnum.AVAILABLE,
        )
        self.ownedCars.append(newCar)

    def delete_car(self, car_id: int) -> None:
        for item in self.ownedCars:
            if item.car.id == car_id:
                self.ownedCars.remove(item)

    def update_car(self, car_id: int, updateCarDTO: Car) -> None:
        for item in self.ownedCars:
            if item.car.id == car_id:
                item.car.brand = updateCarDTO.brand
                item.car.model = updateCarDTO.model
                item.car.year = updateCarDTO.year

    def get_available_cars(self) -> list[StoreItem]:
        return [
            item.car
            for item in self.ownedCars
            if item.status == RentStatusEnum.AVAILABLE
        ]

    def find_available_car(self, car_id) -> RentStatusEnum | bool:
        for item in self.ownedCars:
            if car_id == item.car.id and item.status == RentStatusEnum.AVAILABLE:
                return RentStatusEnum.AVAILABLE

            elif car_id == item.car.id and item.status == RentStatusEnum.RENTED:
                return RentStatusEnum.RENTED

        return False
