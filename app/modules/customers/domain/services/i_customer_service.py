from abc import ABC, abstractmethod
from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


class ICustomerService(ABC):
    @abstractmethod
    def get_all_customers(self) -> list[Customer]: ...

    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer: ...

    @abstractmethod
    def add_customer(self, create_customer_dto: CreateCustomerDTO) -> int: ...

    @abstractmethod
    def delete_customer(self, customer_id: int) -> int: ...

    @abstractmethod
    def update_customer(
        self, customer_id: int, update_customer_dto: UpdateCustomerDTO
    ) -> int: ...

    @abstractmethod
    def block_customer(self, customer_id: int) -> int: ...

    @abstractmethod
    def unlock_customer(self, customer_id: int) -> int: ...
