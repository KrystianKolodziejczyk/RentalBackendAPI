from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO
from app.shared.infrastructure.services.fake_database.fake_database import FakeDatabse
from app.modules.customers.infrastrucutre.mappers.customer_mapper import CustomerMapper
from pathlib import Path


class CustomerRepositoryV2(ICustomerRepository):
    path: Path
    generalId: int

    def __init__(self):
        self.path = Path("database/customers.json")
        self.generalId = 0

    # Helper
    def _parse_and_save(self, customers: list[Customer]) -> None:
        customersDictList: list[dict] = [
            CustomerMapper.customer_to_json(customer=oneCustomer)
            for oneCustomer in customers
        ]

        FakeDatabse.save_json_list(
            path=self.path,
            pythonData=customersDictList,
        )

    # Returns all customers
    def get_all_customers(self) -> list[Customer]:
        customers: list[dict] = FakeDatabse.get_json_list(path=self.path)
        return [
            CustomerMapper.json_to_customer(customerDict=oneCustomer)
            for oneCustomer in customers
        ]

    # Returns one customer
    def get_customer_by_id(self, customer_id: int) -> Customer:
        customers: list[Customer] = self.get_all_customers()
        for oneCustomer in customers:
            if oneCustomer.id == customer_id:
                return oneCustomer

        return None

    # Adds customer
    def add_customer(self, newId: int, createCustomerDTO: CreateCustomerDTO) -> None:
        customers: list[Customer] = self.get_all_customers()
        customers.append(
            Customer(
                id=newId,
                name=createCustomerDTO.name,
                lastName=createCustomerDTO.last_name,
                phoneNumber=createCustomerDTO.phone_number,
                driverLicenseId=createCustomerDTO.driver_license_id,
                status=CustomerStatusEnum.UNLOCKED,
            )
        )

        self._parse_and_save(customers=customers)

    # Deletes customer
    def delete_customer(self, customer_id: int) -> None:
        customers: list[Customer] = self.get_all_customers()
        for oneCustomer in customers:
            if oneCustomer.id == customer_id:
                customers.remove(oneCustomer)

        self._parse_and_save(customers=customers)

    # Updated customer
    def update_customer(
        self, customer_id: int, updateCustomerDTO: UpdateCustomerDTO
    ) -> None:
        customers: list[Customer] = self.get_all_customers()
        for oneCustomer in customers:
            if oneCustomer.id == customer_id:
                oneCustomer.name = updateCustomerDTO.name
                oneCustomer.last_name = updateCustomerDTO.last_name
                oneCustomer.phone_number = updateCustomerDTO.phone_number
                oneCustomer.driver_license_id = updateCustomerDTO.driver_license_id

        self._parse_and_save(customers=customers)

    # Blocks customer
    def block_customer(self, customer_id: int) -> None:
        customers: list[Customer] = self.get_all_customers()
        for oneCustomer in customers:
            if oneCustomer.id == customer_id:
                oneCustomer.status = CustomerStatusEnum.BLOCKED

        self._parse_and_save(customers=customers)

    # Unlocks customer
    def unlock_customer(self, customer_id) -> None:
        customers: list[Customer] = self.get_all_customers()
        for oneCustomer in customers:
            if oneCustomer.id == customer_id:
                oneCustomer.status = CustomerStatusEnum.UNLOCKED

        self._parse_and_save(customers=customers)
