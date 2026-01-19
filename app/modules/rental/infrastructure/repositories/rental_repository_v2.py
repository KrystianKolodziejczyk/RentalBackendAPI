from pathlib import Path
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.domain.repositories.i_rental_repository_v2 import (
    IRentalRepositoryV2,
)
from app.shared.infrastructure.services.fake_database.fake_database import FakeDatabse
from app.modules.rental.infrastructure.mappers.store_item_mapper import StoreItemMapper


# Storehouse Class
class RentalRepositoryV2(IRentalRepositoryV2):
    path: Path

    def __init__(self, path: Path) -> None:
        self.path = path

    # Returns list of all instances
    def get_all(self) -> list[StoreItem]:
        store_items: list[dict] = FakeDatabse.get_json_list(path=self.path)
        return [
            StoreItemMapper.json_to_store_item(store_item_dict=one_store_item)
            for one_store_item in store_items
        ]

    def save_all(self, store_item_list: list[StoreItem]) -> None:
        store_items_list_dict: list[dict] = [
            StoreItemMapper.store_item_to_json(one_store_item)
            for one_store_item in store_item_list
        ]

        FakeDatabse.save_json_list(path=self.path, python_data=store_items_list_dict)
