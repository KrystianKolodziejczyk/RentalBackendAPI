from abc import ABC, abstractmethod
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


class ICustomerRepository(ABC):
    @abstractmethod
    def get_all_customers(self) -> list[Customer]: ...

    @abstractmethod
    def get_one_customer(self, customer_id: int) -> Customer: ...

    @abstractmethod
    def add_customer(
        self, newId: int, createCustomerDTO: CreateCustomerDTO
    ) -> None: ...

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None: ...

    @abstractmethod
    def update_customer(
        self, customer_id: int, updateCustomerDTO: UpdateCustomerDTO
    ) -> None: ...

    @abstractmethod
    def block_customer(self, customer_id: int) -> None: ...

    @abstractmethod
    def unlock_customer(self, customer_id: int) -> None: ...
