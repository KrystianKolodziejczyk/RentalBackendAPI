from abc import ABC, abstractmethod
from app.modules.inventory.domain.models.store_item import StoreItem


class IInventoryRepositoryV2(ABC):
    @abstractmethod
    def get_all(self) -> list[StoreItem]: ...

    @abstractmethod
    def save_all(self, store_item_list: list[StoreItem]) -> None: ...
