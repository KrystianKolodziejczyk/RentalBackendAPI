from fastapi import HTTPException, status
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.presentation.dto import (
    CreateCarDTO,
    UpdateCarDTO,
)


class RentalService(IRentalService):
    def __init__(self, rental_repository: IRentalRepository):
        self.rental_repository: IRentalRepository = rental_repository

    # Returns all store items instances
    def get_all_cars(self) -> list[StoreItem]:
        allCars = self.rental_repository.get_all_cars()
        return [car.car for car in allCars]

    # Returns one store item instance by id
    def get_car_by_id(self, car_id: int) -> Car:
        item: StoreItem = self.rental_repository.get_car_by_id(car_id)
        if item:
            return item.car

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Returns quantity of all store items
    def get_all_cars_qty(self) -> int:
        return self.rental_repository.get_all_cars_qty()

    # Adds new store item instance
    def add_car(self, createCarDTO: CreateCarDTO) -> int:
        self.rental_repository.generalId += 1
        newId: int = self.rental_repository.generalId

        self.rental_repository.add_car(
            car=Car(
                id=newId,
                brand=createCarDTO.brand,
                model=createCarDTO.model,
                year=createCarDTO.year,
            )
        )

        return newId

    # Deletes one store item instance
    def delete_car(self, car_id: int) -> int:
        item: StoreItem = self.rental_repository.get_car_by_id(car_id=car_id)
        if item:
            if item.status == RentStatusEnum.RENTED:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="cant_delete_rented_car",
                )

            elif item.status == RentStatusEnum.AVAILABLE:
                self.rental_repository.delete_car(car_id=car_id)
                return car_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Updates selected car info
    def update_car(
        self,
        car_id: int,
        updateCarDTO: UpdateCarDTO,
    ) -> int:
        item: StoreItem = self.rental_repository.get_car_by_id(car_id=car_id)
        if item:
            if item.status == RentStatusEnum.RENTED:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="cant_change_rented_car!",
                )

            elif item.status == RentStatusEnum.AVAILABLE:
                item.car.brand = updateCarDTO.brand
                item.car.model = updateCarDTO.model
                item.car.year = updateCarDTO.year

                return car_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Returns only available store items
    def get_available_cars(self) -> list[StoreItem]:
        availableCars = self.rental_repository.get_available_cars()
        if availableCars:
            return availableCars

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="no_available_cars"
        )

    # Checks and returns availabilty of one car
    def check_car_availability(self, car_id) -> RentStatusEnum:
        availableCar: str = self.rental_repository.find_available_car(car_id=car_id)
        if availableCar:
            return availableCar

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Changes item's status to Rented
    def rent_car(self, car_id: int) -> RentStatusEnum:
        item = self.rental_repository.get_car_by_id(car_id=car_id)
        if item:
            if item.status == RentStatusEnum.RENTED:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="car_already_rented",
                )

            elif item.status == RentStatusEnum.AVAILABLE:
                item.status = RentStatusEnum.RENTED
                return RentStatusEnum.RENTED

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    def return_car(self, car_id) -> RentStatusEnum:
        item = self.rental_repository.get_car_by_id(car_id=car_id)
        if item:
            if item.status == RentStatusEnum.AVAILABLE:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="this_car_is_not_rented",
                )

            elif item.status == RentStatusEnum.RENTED:
                item.status = RentStatusEnum.AVAILABLE
                return RentStatusEnum.AVAILABLE

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )
