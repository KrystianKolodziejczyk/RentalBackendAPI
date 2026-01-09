from fastapi import HTTPException, status
from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


class CustomerService(ICustomerService):
    def __init__(self, customerRepository: ICustomerRepository):
        self.customer_repository = customerRepository

    # Returns all customers list
    def get_all_customers(self) -> list[Customer]:
        customers: list[Customer] = self.customer_repository.get_all_customers()
        if customers:
            return customers

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customers_list_is_empty!"
        )

    # Returns customer
    def get_customer_by_id(self, customer_id: int) -> Customer:
        customer: Customer = self.customer_repository.get_one_customer(customer_id)
        if customer:
            return customer

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer_doesnt_exist!"
        )

    # Adds customer, creates new ID, returns ID
    def add_customer(self, createCustomerDTO: CreateCustomerDTO) -> int:
        self.customer_repository.generalId += 1
        newId: int = self.customer_repository.generalId

        self.customer_repository.add_customer(
            newId=newId, createCustomerDTO=createCustomerDTO
        )
        return newId

    # Deletes customer, returns ID
    def delete_customer(self, customer_id: int) -> int:
        customer: Customer = self.customer_repository.get_one_customer(customer_id)
        if customer:
            self.customer_repository.delete_customer(customer_id=customer_id)
            return customer_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer_doesnt_exitst!"
        )

    # Updates customer, returns ID
    def update_customer(
        self, customer_id: int, updateCustomerDTO: UpdateCustomerDTO
    ) -> int:
        customer: Customer = self.customer_repository.get_one_customer(customer_id)
        if customer:
            if customer.phoneNumber in [
                customer.phoneNumber for customer in self.customer_repository.customers
            ]:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="phone_number_already_in_database",
                )

            if customer.driverLicenseId in [
                customer.driverLicenseId
                for customer in self.customer_repository.customers
            ]:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="driver_license_id_already_in_database",
                )

            self.customer_repository.update_customer(
                customer_id=customer_id, updateCustomerDTO=updateCustomerDTO
            )
            return customer_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer_doesnt_exitst!"
        )

    # Blocks customer, returns ID
    def block_customer(self, customer_id: int) -> int:
        customer: Customer = self.customer_repository.get_one_customer(customer_id)
        if customer:
            if customer.status == CustomerStatusEnum.BLOCKED:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="customer_already_blocked!",
                )

            elif customer.status == CustomerStatusEnum.UNLOCKED:
                self.customer_repository.block_customer(customer_id=customer_id)
                return customer_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer_doesnt_exist!"
        )

    # Unlocks customer, returns ID
    def unlock_customer(self, customer_id: int) -> int:
        customer: Customer = self.customer_repository.get_one_customer(
            customer_id=customer_id
        )
        if customer:
            if customer.status == CustomerStatusEnum.UNLOCKED:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="customer_cant_be_unlocked_when_is_active!",
                )

            elif customer.status == CustomerStatusEnum.BLOCKED:
                self.customer_repository.unlock_customer(customer_id=customer_id)
                return customer_id

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer_doesnt_exist!"
        )
