from fastapi import HTTPException, status
from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO
from app.modules.customers.domain.exceptions.customer_excpetions import (
    CustomerNotFoundExcpetion,
    PhoneNumberInDatabesException,
    DriverLicenseInDatabaseExpetion,
    CustomerAlreadyBlockedException,
    CustomerAlreadyUnlockedException,
)


class CustomerServiceV2(ICustomerService):
    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    # Helper
    def _find_by_id(
        self, customers_list: list[Customer], customer_id: int
    ) -> Customer | None:
        for one_customer in customers_list:
            if one_customer.id == customer_id:
                return one_customer

        raise CustomerNotFoundExcpetion(customer_id=customer_id)

    # Helper
    def _get_last_id(self, customers_list: list[Customer]) -> int:
        if not customers_list:
            return 1

        return max(one_customer.id for one_customer in customers_list) + 1

    # Helper
    def _get_all_and_find(self, customer_id: int) -> tuple[list[Customer], Customer]:
        all_customers: list[Customer] = self.customer_repository.get_all()
        one_customer: Customer = self._find_by_id(
            customers_list=all_customers, customer_id=customer_id
        )
        return all_customers, one_customer

    # Returns all customers list
    def get_all_customers(self) -> list[Customer]:
        return self.customer_repository.get_all()

    # Returns customer
    def get_customer_by_id(self, customer_id: int) -> Customer | None:
        _, one_customer = self._get_all_and_find(customer_id=customer_id)
        return one_customer

    # Adds customer, creates new ID, returns ID
    def add_customer(self, create_customer_dto: CreateCustomerDTO) -> int:
        all_customers: list[Customer] = self.customer_repository.get_all()
        for one_customer in all_customers:
            if one_customer.phone_number == create_customer_dto.phone_number:
                raise PhoneNumberInDatabesException(
                    phone_number=create_customer_dto.phone_number
                )
            if one_customer.driver_license_id == create_customer_dto.driver_license_id:
                raise DriverLicenseInDatabaseExpetion(
                    driver_license_id=create_customer_dto.driver_license_id
                )

        new_id: int = self._get_last_id(customers_list=all_customers)

        all_customers.append(
            Customer(
                id=new_id,
                name=create_customer_dto.name,
                last_name=create_customer_dto.last_name,
                phone_number=create_customer_dto.phone_number,
                driver_license_id=create_customer_dto.driver_license_id,
                status=CustomerStatusEnum.UNLOCKED,
            )
        )

        self.customer_repository.save_all(customers_list=all_customers)
        return new_id

    # Deletes customer, returns ID
    def delete_customer(self, customer_id: int) -> int:
        all_customers, one_customer = self._get_all_and_find(customer_id=customer_id)

        all_customers: list[Customer] = [
            one_customer
            for one_customer in all_customers
            if one_customer.id != customer_id
        ]
        self.customer_repository.save_all(customers_list=all_customers)
        return customer_id

    # Updates customer, returns ID
    def update_customer(
        self, customer_id: int, update_customer_dto: UpdateCustomerDTO
    ) -> int:
        all_customers, one_customer = self._get_all_and_find(customer_id=customer_id)

        for c in all_customers:
            if (
                c.phone_number == update_customer_dto.phone_number
                and c.id != customer_id
            ):
                raise PhoneNumberInDatabesException(
                    phone_number=update_customer_dto.phone_number
                )
            if (
                c.driver_license_id == update_customer_dto.driver_license_id
                and c.id != customer_id
            ):
                raise DriverLicenseInDatabaseExpetion(
                    driver_license_id=update_customer_dto.driver_license_id
                )

        one_customer.name = update_customer_dto.name
        one_customer.last_name = update_customer_dto.last_name
        one_customer.phone_number = update_customer_dto.phone_number
        one_customer.driver_license_id = update_customer_dto.driver_license_id

        self.customer_repository.save_all(customers_list=all_customers)
        return customer_id

    # Blocks customer, returns ID
    def block_customer(self, customer_id: int) -> int:
        all_customers, one_customer = self._get_all_and_find(customer_id=customer_id)

        if one_customer.status != CustomerStatusEnum.BLOCKED:
            one_customer.status = CustomerStatusEnum.BLOCKED
            self.customer_repository.save_all(customers_list=all_customers)
            return customer_id

        raise CustomerAlreadyBlockedException(customer_id=customer_id)

    # Unlocks customer, returns ID
    def unlock_customer(self, customer_id: int) -> int:
        all_customers, one_customer = self._get_all_and_find(customer_id=customer_id)

        if one_customer.status != CustomerStatusEnum.UNLOCKED:
            one_customer.status = CustomerStatusEnum.UNLOCKED
            self.customer_repository.save_all(customers_list=all_customers)
            return customer_id

        raise CustomerAlreadyUnlockedException(customer_id=customer_id)
