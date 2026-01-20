from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.repositories.i_inventory_repository_v2 import (
    IInventoryRepositoryV2,
)
from app.modules.inventory.domain.services.i_inventory_service import IInventoryService
from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.inventory.presentation.dto import (
    CreateCarDTO,
    UpdateCarDTO,
)
from app.modules.inventory.domain.exceptions.inventory_exceptions import (
    CarNotFoundException,
    CarAlreadyRentedException,
    CarIsNotRentedException,
)


class InventoryServiceV2(IInventoryService):
    def __init__(self, inventory_repository: IInventoryRepositoryV2):
        self.inventory_repository: IInventoryRepositoryV2 = inventory_repository

    # Helper, finds car by id
    def _find_by_id(self, cars: list[Car], car_id: int) -> Car:
        for car in cars:
            if car.id == car_id:
                return car
        raise CarNotFoundException(car_id=car_id)

    # Helper, returns tuple
    def _get_all_and_find(self, car_id: int) -> tuple[list[Car], Car]:
        all_cars: list[Car] = self.inventory_repository.get_all()
        one_car: Car = self._find_by_id(cars=all_cars, car_id=car_id)
        return all_cars, one_car

    # Helper, checks rented status
    def _ensure_not_rented(self, car: Car, action: str) -> None:
        if car.status == RentStatusEnum.RENTED:
            raise CarAlreadyRentedException(car_id=car.id, action=action)

    # Helper, gets next available id
    def _get_next_id(self, cars: list[Car]) -> int:
        if not cars:
            return 1
        return max(car.id for car in cars) + 1

    # Returns all cars
    def get_all_cars(self) -> list[Car]:
        return self.inventory_repository.get_all()

    # Returns one car by id
    def get_car_by_id(self, car_id: int) -> Car:
        _, one_car = self._get_all_and_find(car_id=car_id)
        return one_car

    # Returns quantity of all cars
    def get_all_cars_qty(self) -> int:
        return len(self.inventory_repository.get_all())

    # Adds new car
    def add_car(self, create_car_dto: CreateCarDTO) -> int:
        all_cars: list[Car] = self.inventory_repository.get_all()
        new_id: int = self._get_next_id(cars=all_cars)

        all_cars.append(
            Car(
                id=new_id,
                brand=create_car_dto.brand,
                model=create_car_dto.model,
                year=create_car_dto.year,
                status=RentStatusEnum.AVAILABLE,
            )
        )
        self.inventory_repository.save_all(cars_list=all_cars)
        return new_id

    # Deletes car
    def delete_car(self, car_id: int) -> int:
        all_cars, one_car = self._get_all_and_find(car_id=car_id)
        self._ensure_not_rented(car=one_car, action="delete")

        all_cars = [car for car in all_cars if car.id != car_id]
        self.inventory_repository.save_all(cars_list=all_cars)
        return one_car.id

    # Updates car info
    def update_car(self, car_id: int, update_car_dto: UpdateCarDTO) -> int:
        all_cars, one_car = self._get_all_and_find(car_id=car_id)
        self._ensure_not_rented(car=one_car, action="change")

        one_car.brand = update_car_dto.brand
        one_car.model = update_car_dto.model
        one_car.year = update_car_dto.year

        self.inventory_repository.save_all(cars_list=all_cars)
        return car_id

    # Returns only available cars
    def get_available_cars(self) -> list[Car]:
        all_cars: list[Car] = self.inventory_repository.get_all()
        return [car for car in all_cars if car.status == RentStatusEnum.AVAILABLE]

    # Checks and returns car status
    def check_car_status(self, car_id: int) -> RentStatusEnum:
        _, one_car = self._get_all_and_find(car_id=car_id)
        return one_car.status

    # Rents car
    def rent_car(self, car_id: int) -> RentStatusEnum:
        all_cars, one_car = self._get_all_and_find(car_id=car_id)
        self._ensure_not_rented(car=one_car, action="rent")

        one_car.status = RentStatusEnum.RENTED
        self.inventory_repository.save_all(cars_list=all_cars)
        return one_car.status

    # Returns rented car
    def return_car(self, car_id: int) -> RentStatusEnum:
        all_cars, one_car = self._get_all_and_find(car_id=car_id)
        if one_car.status == RentStatusEnum.AVAILABLE:
            raise CarIsNotRentedException(car_id=car_id)

        one_car.status = RentStatusEnum.AVAILABLE
        self.inventory_repository.save_all(cars_list=all_cars)
        return one_car.status
