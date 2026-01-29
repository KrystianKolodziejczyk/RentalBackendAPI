from abc import ABC, abstractmethod

from app.modules.customers.domain.models.customer import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    async def get_customer_by_id(self, customer_id: int) -> Customer: ...

    @abstractmethod
    async def get_all_customers(self) -> list[Customer]: ...

    @abstractmethod
    async def add_customer(self, customer: Customer) -> int: ...

    @abstractmethod
    async def delete_customer(self, customer_id: int) -> int: ...

    @abstractmethod
    async def update_customer(self, customer_id: int, customer: Customer) -> int: ...

    @abstractmethod
    async def change_status_customer(
        self, customer_id: int, new_status: str
    ) -> int: ...
