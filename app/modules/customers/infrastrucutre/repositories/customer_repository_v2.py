from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


class CustomerRepositoryV2(ICustomerRepository):
    customers: list[Customer]
    generalId: int

    def __init__(self):
        self.customers = []
        self.generalId = 0

    # Returns all customers
    def get_all_customers(self) -> list[Customer]:
        return self.customers

    # Returns one customer
    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

        return None

    # Adds customer
    def add_customer(self, newId: int, createCustomerDTO: CreateCustomerDTO) -> None:
        self.customers.append(
            Customer(
                id=newId,
                name=createCustomerDTO.name,
                lastName=createCustomerDTO.last_name,
                phoneNumber=createCustomerDTO.phone_number,
                status=CustomerStatusEnum.UNLOCKED,
                driverLicenseId=createCustomerDTO.driver_license_id,
            )
        )

    def delete_customer(self, customer_id: int) -> None:
        for customer in self.customers:
            if customer.id == customer_id:
                self.customers.remove(customer)

    # Updated customer
    def update_customer(
        self, customer_id: int, updateCustomerDTO: UpdateCustomerDTO
    ) -> None:
        for customer in self.customers:
            if customer.id == customer_id:
                customer.name = updateCustomerDTO.name
                customer.last_name = updateCustomerDTO.last_name
                customer.phone_number = updateCustomerDTO.phone_number
                customer.driver_license_id = updateCustomerDTO.driver_license_id

    # Blocks customer
    def block_customer(self, customer_id: int) -> None:
        for customer in self.customers:
            if customer.id == customer_id:
                customer.status = CustomerStatusEnum.BLOCKED

    # Unlocks customer
    def unlock_customer(self, customer_id) -> None:
        for customer in self.customers:
            if customer.id == customer_id:
                customer.status = CustomerStatusEnum.UNLOCKED
