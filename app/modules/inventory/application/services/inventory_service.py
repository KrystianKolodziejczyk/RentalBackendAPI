from fastapi import HTTPException, status
from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.models.store_item import StoreItem
from app.modules.inventory.domain.repositories.i_inventory_repository import IInventoryRepository
from app.modules.inventory.domain.services.i_inventory_service import IInventoryService
from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.inventory.presentation.dto import (
    CreateCarDTO,
    UpdateCarDTO,
)


class InventoryService(IInventoryService):
    def __init__(self, inventory_repository: IInventoryRepository):
        self.inventory_repository: IInventoryRepository = inventory_repository

    # Returns all store items instances
    def get_all_cars(self) -> list[StoreItem]:
        allCars = self.inventory_repository.get_all_cars()
        return [car.car for car in allCars]

    # Returns one store item instance by id
    def get_storeItem_by_id(self, car_id: int) -> StoreItem:
        oneStoreItem: StoreItem = self.inventory_repository.get_storeItem_by_id(car_id)
        if oneStoreItem:
            return oneStoreItem

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="car_doesn't_exist"
        )

    # Returns quantity of all store items
    def get_all_cars_qty(self) -> int:
        return self.inventory_repository.get_all_cars_qty()

    # Adds new store item instance
    def add_car(self, createCarDTO: CreateCarDTO) -> int:
        self.inventory_repository.generalId += 1
        newId: int = self.inventory_repository.generalId

        self.inventory_repository.add_car(createCarDTO=createCarDTO, newId=newId)

        return newId

    # Deletes one store item instance
    def delete_car(self, car_id: int) -> int:
        oneStoreItem: StoreItem = self.get_storeItem_by_id(car_id=car_id)
        if not oneStoreItem.status == RentStatusEnum.RENTED:
            self.inventory_repository.delete_car(car_id=car_id)
            return car_id

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="cant_delete_rented_car",
        )

    # Updates selected car info
    def update_car(self, car_id: int, updateCarDTO: UpdateCarDTO) -> int:
        oneStoreItem: StoreItem = self.get_storeItem_by_id(car_id=car_id)
        if not oneStoreItem.status == RentStatusEnum.RENTED:
            self.inventory_repository.update_car(car_id=car_id, updateCarDTO=updateCarDTO)
            return car_id

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="cant_change_rented_car!",
        )

    # Returns only available store items
    def get_available_cars(self) -> list[Car]:
        availableItems: list[StoreItem] = self.inventory_repository.get_available_cars(
            RentStatusEnum.AVAILABLE
        )
        if availableItems:
            return [oneItem.car for oneItem in availableItems]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="no_available_cars"
        )

    # Checks and returns availabilty of one car
    def check_car_availability(self, car_id: int) -> RentStatusEnum:
        oneStoreItem: StoreItem = self.get_storeItem_by_id(car_id=car_id)
        return oneStoreItem.status

    # Changes item's status to Rented
    def rent_car(self, car_id: int) -> RentStatusEnum:
        oneItem: StoreItem = self.get_storeItem_by_id(car_id=car_id)
        if not oneItem.status == RentStatusEnum.RENTED:
            oneItem.status = RentStatusEnum.RENTED
            return oneItem.status

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="car_already_rented",
        )

    def return_car(self, car_id: int) -> RentStatusEnum:
        oneItem: StoreItem = self.get_storeItem_by_id(car_id=car_id)
        if not oneItem.status == RentStatusEnum.AVAILABLE:
            oneItem.status = RentStatusEnum.AVAILABLE
            return oneItem.status

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="car_already_rented",
        )
