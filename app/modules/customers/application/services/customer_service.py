from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.exceptions.customer_exceptions import (
    CustomerAlreadyBlockedException,
    CustomerNotFoundException,
    DriverLicenseInDatabaseException,
    PhoneNumberInDatabaseException,
)
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


class CustomerService(ICustomerService):
    _customer_repository: ICustomerRepository

    def __init__(self, customer_repository: ICustomerRepository) -> None:
        self._customer_repository = customer_repository

    # Helper gets customer and checks existence
    async def _get_customer_and_check(self, customer_id: int) -> Customer:
        customer: Customer = await self._customer_repository.get_customer_by_id(
            customer_id=customer_id
        )
        if customer is None:
            raise CustomerNotFoundException(customer_id=customer_id)

        return customer

    # Returns one customer
    async def get_customer_by_id(self, customer_id: int) -> Customer:
        return await self._get_customer_and_check(customer_id=customer_id)

    # Returns all customers
    async def get_all_customers(self) -> list[Customer]:
        return await self._customer_repository.get_all_customers()

    # Adds new customer
    async def add_customer(self, create_customer_dto: CreateCustomerDTO) -> int:
        new_id: int = await self._customer_repository.add_customer(
            customer=Customer.create(
                id=None,
                name=create_customer_dto.name,
                last_name=create_customer_dto.last_name,
                phone_number=create_customer_dto.phone_number,
                driver_license_id=create_customer_dto.driver_license_id,
                status=CustomerStatusEnum.UNLOCKED,
            )
        )

        return new_id

    # Deletes customer
    async def delete_customer(self, customer_id: int) -> int:
        customer: Customer = await self._get_customer_and_check(customer_id=customer_id)
        if customer.status == CustomerStatusEnum.BLOCKED:
            raise CustomerAlreadyBlockedException(customer_id=customer_id)

        await self._customer_repository.delete_customer(customer_id=customer_id)
        return customer_id

    # Updates customer
    async def update_customer(
        self, customer_id: int, update_customer_dto: UpdateCustomerDTO
    ) -> int:
        customer: Customer = await self._get_customer_and_check(customer_id=customer_id)

        customer.update(
            name=update_customer_dto.name,
            last_name=update_customer_dto.last_name,
            phone_number=update_customer_dto.phone_number,
            driver_license_id=update_customer_dto.driver_license_id,
        )

        try:
            await self._customer_repository.update_customer(
                customer_id=customer_id, customer=customer
            )
            return customer_id

        except PhoneNumberInDatabaseException:
            raise

        except DriverLicenseInDatabaseException:
            raise

    # Blocks customer
    async def block_customer(self, customer_id: int) -> int:
        customer: Customer = await self._get_customer_and_check(customer_id=customer_id)
        customer.block()

        return await self._customer_repository.change_status_customer(
            customer_id=customer_id, customer=customer
        )

    # Unlocks customer
    async def unlock_customer(self, customer_id: int) -> int:
        customer: Customer = await self._get_customer_and_check(customer_id=customer_id)
        customer.unlock()

        return await self._customer_repository.change_status_customer(
            customer_id=customer_id, customer=customer
        )
