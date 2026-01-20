from abc import ABC, abstractmethod
from app.modules.inventory.domain.models.car import Car


class IInventoryRepositoryV2(ABC):
    @abstractmethod
    def get_all(self) -> list[Car]: ...

    @abstractmethod
    def save_all(self, cars_list: list[Car]) -> None: ...
