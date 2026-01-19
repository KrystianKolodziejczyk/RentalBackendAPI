from abc import ABC, abstractmethod
from app.modules.customers.domain.models.customer import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Customer]: ...

    @abstractmethod
    def save_all(self, customers_list: list[Customer]) -> None: ...
