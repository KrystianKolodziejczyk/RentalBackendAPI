from abc import ABC, abstractmethod

from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


class ICustomerService(ABC):
    @abstractmethod
    async def get_customer_by_id(self, customer_id: int) -> Customer: ...

    @abstractmethod
    async def get_all_customers(self) -> list[Customer]: ...

    @abstractmethod
    async def add_customer(self, create_customer_dto: CreateCustomerDTO) -> int: ...

    @abstractmethod
    async def delete_customer(self, customer_id: int) -> int: ...

    @abstractmethod
    async def update_customer(
        self, customer_id: int, update_customer_dto: UpdateCustomerDTO
    ) -> int: ...

    @abstractmethod
    async def block_customer(self, customer_id: int) -> str: ...

    @abstractmethod
    async def unlock_customer(self, customer_id: int) -> str: ...
