from pathlib import Path
from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.repositories.i_inventory_repository_v2 import (
    IInventoryRepositoryV2,
)
from app.shared.infrastructure.services.fake_database.fake_database import FakeDatabse
from app.modules.inventory.infrastructure.mappers.car_mapper import CarMapper


class InventoryRepositoryV2(IInventoryRepositoryV2):
    path: Path

    def __init__(self, path: Path) -> None:
        self.path = path

    def get_all(self) -> list[Car]:
        cars_dict: list[dict] = FakeDatabse.get_json_list(path=self.path)
        return [CarMapper.json_to_car(car_dict=one_car) for one_car in cars_dict]

    def save_all(self, cars_list: list[Car]) -> None:
        cars_list_dict: list[dict] = [
            CarMapper.car_to_json(one_car) for one_car in cars_list
        ]
        FakeDatabse.save_json_list(path=self.path, python_data=cars_list_dict)
