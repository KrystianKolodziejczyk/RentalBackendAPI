from pathlib import Path
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.shared.infrastructure.services.fake_database.fake_database import FakeDatabse
from app.modules.rental.infrastructure.mappers.store_item_mapper import StoreItemMapper


# Storehouse Class
class RentalRepositoryV2(IRentalRepository):
    ownedCars: list[StoreItem]
    generalId: int
    path: Path

    def __init__(self) -> None:
        self.ownedCars = []
        self.generalId = 0
        self.path = Path("database/store_item.json")

    # Returns list of all instances
    def get_all_cars(self) -> list[StoreItem]:
        storeItems: list[dict] = FakeDatabse.get_json_list(path=self.path)
        return [
            StoreItemMapper.json_to_storeItem(storeItemDict=oneStoreItem)
            for oneStoreItem in storeItems
        ]

    # Returns store's item instance
    def get_storeItem_by_id(self, car_id: int) -> StoreItem:
        allStoreItems: list[StoreItem] = self.get_all_cars()
        for oneItem in allStoreItems:
            if oneItem.car.id == car_id:
                return oneItem

        return None

    def get_all_cars_qty(self) -> int:
        return int(len(self.get_all_cars()))

    def add_car(self, createCarDTO: Car, newId: int) -> None:
        allStoreItems: list[StoreItem] = self.get_all_cars()
        allStoreItems.append(
            StoreItem(
                car=Car(
                    id=newId,
                    brand=createCarDTO.brand,
                    model=createCarDTO.model,
                    year=createCarDTO.year,
                ),
                status=RentStatusEnum.AVAILABLE,
            )
        )

        storeItemListDicts: list[dict] = [
            StoreItemMapper.storeItem_to_json(storeItem=oneStoreItem)
            for oneStoreItem in allStoreItems
        ]

        FakeDatabse.save_json_list(path=self.path, pythonData=storeItemListDicts)

    def delete_car(self, car_id: int) -> None:
        allStoreItems: list[StoreItem] = self.get_all_cars()
        for oneStoreItem in allStoreItems:
            if oneStoreItem.car.id == car_id:
                allStoreItems.remove(oneStoreItem)

        storeItemListDicts: list[dict] = [
            StoreItemMapper.storeItem_to_json(storeItem=oneStoreItem)
            for oneStoreItem in allStoreItems
        ]

        FakeDatabse.save_json_list(path=self.path, pythonData=storeItemListDicts)

    def update_car(self, car_id: int, updateCarDTO: Car) -> None:
        allStoreItems: list[StoreItem] = self.get_all_cars()
        for oneStoreItem in allStoreItems:
            if oneStoreItem.car.id == car_id:
                oneStoreItem.car.brand = updateCarDTO.brand
                oneStoreItem.car.model = updateCarDTO.model
                oneStoreItem.car.year = updateCarDTO.year

        storeItemListDicts: list[dict] = [
            StoreItemMapper.storeItem_to_json(storeItem=oneStoreItem)
            for oneStoreItem in allStoreItems
        ]

        FakeDatabse.save_json_list(path=self.path, pythonData=storeItemListDicts)

    def get_available_cars(self, status: RentStatusEnum) -> list[StoreItem]:
        allStoreItems: list[StoreItem] = self.get_all_cars()
        return [
            oneStoreItem
            for oneStoreItem in allStoreItems
            if oneStoreItem.status == status
        ]
