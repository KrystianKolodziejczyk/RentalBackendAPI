from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.models.store_item import StoreItem
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

    # Helper, finds item by id
    def _find_by_id(self, items: list[StoreItem], car_id: int) -> StoreItem | None:
        for item in items:
            if item.car.id == car_id:
                return item

        raise CarNotFoundException(car_id=car_id)

    # Helper, returns tuple
    def _get_all_and_find(self, car_id: int) -> tuple[list[StoreItem], StoreItem]:
        all_items: list[StoreItem] = self.inventory_repository.get_all()
        one_item: StoreItem = self._find_by_id(items=all_items, car_id=car_id)
        return all_items, one_item

    # Helper, checks rented status
    def _ensure_rent_status(self, item: StoreItem, action: str) -> None:
        if item.status == RentStatusEnum.RENTED:
            raise CarAlreadyRentedException(car_id=item.car.id, action=action)

    def _get_last_id(self, item_list: list[StoreItem]) -> int:
        if not item_list:
            return 1

        return max(item.car.id for item in item_list) + 1

    # Returns all store items instances
    def get_all_cars(self) -> list[Car]:
        all_cars = self.inventory_repository.get_all()
        return [car.car for car in all_cars]

    # Returns one car instance by id
    def get_store_item_by_id(self, car_id: int) -> Car:
        _, one_item = self._get_all_and_find(car_id=car_id)
        return one_item.car

    # Returns quantity of all store items
    def get_all_cars_qty(self) -> int:
        return int(len(self.inventory_repository.get_all()))

    # Adds new store item instance
    def add_car(self, create_car_dto: CreateCarDTO) -> int:
        all_items: list[StoreItem] = self.inventory_repository.get_all()
        new_id: int = self._get_last_id(item_list=all_items)

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
        self.inventory_repository.save_all(store_item_list=all_items)

        return new_id

    # Deletes one store item instance
    def delete_car(self, car_id: int) -> int:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        self._ensure_rent_status(item=one_item, action="delete")

        all_items: list[StoreItem] = [
            item for item in all_items if item.car.id != car_id
        ]
        self.inventory_repository.save_all(store_item_list=all_items)
        return one_item.car.id

    # Updates selected car info
    def update_car(self, car_id: int, update_car_dto: UpdateCarDTO) -> int:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        self._ensure_rent_status(item=one_item, action="change")

        one_item.car.brand = update_car_dto.brand
        one_item.car.model = update_car_dto.model
        one_item.car.year = update_car_dto.year

        self.inventory_repository.save_all(store_item_list=all_items)
        return car_id

    # Returns only available store items
    def get_available_cars(self) -> list[Car]:
        all_items: list[StoreItem] = self.inventory_repository.get_all()
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
        self.inventory_repository.save_all(store_item_list=all_items)
        return one_item.status

    # Returns rented car
    def return_car(self, car_id: int) -> RentStatusEnum:
        all_items, one_item = self._get_all_and_find(car_id=car_id)
        if one_item.status == RentStatusEnum.AVAILABLE:
            raise CarIsNotRentedException(car_id=car_id)

        one_item.status = RentStatusEnum.AVAILABLE
        self.inventory_repository.save_all(store_item_list=all_items)
        return one_item.status
