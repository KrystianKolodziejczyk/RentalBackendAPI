from fastapi import HTTPException, status
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum


class RentalService(IRentalService):
    def __init__(self, rental_repository: IRentalRepository):
        self.rental_repository: IRentalRepository = rental_repository

    # Returns all store items instances
    def get_all_cars(self) -> list[StoreItem]:
        return self.rental_repository.get_all_cars()

    # Returns one store item instance by id
    def get_car_by_id(self, car_id: int) -> StoreItem:
        item = self.rental_repository.get_car_by_id(car_id=car_id)
        if item:
            return item

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Returns quantity of all store items
    def get_all_cars_qty(self) -> int:
        return self.rental_repository.get_all_cars_qty()

    # Adds new store item instance
    def add_car(self, createCarDTO):
        pass

    # Deletes one store item instance
    def delete_car(self, car_id: int) -> int:
        result = self.rental_repository.delete_car(car_id=car_id)
        if result:
            return car_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Returns only available store items
    def get_available_cars(self) -> list[StoreItem]:
        availableItems = self.rental_repository.get_available_cars()
        if availableItems:
            return availableItems

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="no_available_cars"
        )

    # Checks and returns availabilty of one car
    def find_availabile_car_by_id(self, car_id):
        availableItem = self.rental_repository.find_availabile_car_by_id(car_id=car_id)
        if availableItem:
            return availableItem

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    def rent_car(self, car_id):
        for item in self.rental_repository.ownedCars:
            if item.car.id == car_id:
                item.status = RentStatusEnum.RENTED
                return car_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    def return_car(self, car_id):
        for item in self.rental_repository.ownedCars:
            if item.car.id == car_id:
                item.status = RentStatusEnum.AVAILABLE
                return car_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )
