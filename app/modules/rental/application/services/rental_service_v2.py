from fastapi import HTTPException, status
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository_v2 import (
    IRentalRepositoryV2,
)
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.presentation.dto import (
    CreateCarDTO,
    UpdateCarDTO,
)


class RentalServiceV2(IRentalService):
    def __init__(self, rental_repository: IRentalRepositoryV2):
        self.rental_repository: IRentalRepositoryV2 = rental_repository

    # Helper, finds item by id
    def _find_by_id(self, items: list[StoreItem], car_id: int) -> StoreItem | None:
        for item in items:
            if item.car.id == car_id:
                return item

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesnt_exist"
        )

    # Helper, returns tuple
    def _get_all_and_find(self, car_id: int) -> tuple[list[StoreItem], StoreItem]:
        all_items: list[StoreItem] = self.rental_repository.get_all()
        one_item: StoreItem = self._find_by_id(items=all_items, car_id=car_id)
        return all_items, one_item

    # Helper, checks rented status
    def _ensure_rent_status(self, item: StoreItem, action: str) -> None:
        if item.status == RentStatusEnum.RENTED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"cant_{action}_rented_car!",
            )

    # Returns all store items instances
    def get_all_cars(self) -> list[Car]:
        all_cars = self.rental_repository.get_all()
        return [car.car for car in all_cars]

    # Returns one car instance by id
    def get_store_item_by_id(self, car_id: int) -> Car:
        _, one_item = self._get_all_and_find(car_id=car_id)
        return one_item.car

    # Returns quantity of all store items
    def get_all_cars_qty(self) -> int:
        return int(len(self.rental_repository.get_all()))

    # Adds new store item instance
    def add_car(self, create_car_dto: CreateCarDTO) -> int:
        self.rental_repository.general_id += 1
        new_id: int = self.rental_repository.general_id

        all_items: list[StoreItem] = self.rental_repository.get_all()
        all_items.append(
            StoreItem(
                car=Car(
                    id=new_id,
                    brand=create_car_dto.brand,
                    model=create_car_dto.model,
                    year=create_car_dto.year,
                ),
                status=RentStatusEnum.AVAILABLE,
            )
        )
        self.rental_repository.save_all(store_item_list=all_items)

        return new_id

    # Deletes one store item instance
    def delete_car(self, car_id: int) -> int:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        self._ensure_rent_status(item=one_item, action="delete")

        all_items: list[StoreItem] = [
            item for item in all_items if item.car.id != car_id
        ]
        self.rental_repository.save_all(store_item_list=all_items)
        return one_item.car.id

    # Updates selected car info
    def update_car(self, car_id: int, update_car_dto: UpdateCarDTO) -> int:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        self._ensure_rent_status(item=one_item, action="change")

        one_item.car.brand = update_car_dto.brand
        one_item.car.model = update_car_dto.model
        one_item.car.year = update_car_dto.year

        self.rental_repository.save_all(store_item_list=all_items)
        return car_id

    # Returns only available store items
    def get_available_cars(self) -> list[Car]:
        all_items: list[StoreItem] = self.rental_repository.get_all()
        return [
            item.car for item in all_items if item.status == RentStatusEnum.AVAILABLE
        ]

    # Checks and returns availability of one car
    def check_car_status(self, car_id: int) -> RentStatusEnum:
        _, one_item = self._get_all_and_find(car_id=car_id)
        return one_item.status

    # Changes item's status to Rented
    def rent_car(self, car_id: int) -> RentStatusEnum:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        self._ensure_rent_status(item=one_item, action="rent")

        one_item.status = RentStatusEnum.RENTED
        self.rental_repository.save_all(store_item_list=all_items)
        return one_item.status

    def return_car(self, car_id: int) -> RentStatusEnum:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        if one_item.status == RentStatusEnum.AVAILABLE:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="cant_return_unrented_car!",
            )

        one_item.status = RentStatusEnum.AVAILABLE
        self.rental_repository.save_all(store_item_list=all_items)
        return one_item.status
