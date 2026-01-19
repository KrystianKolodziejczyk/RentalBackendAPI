from fastapi import HTTPException, status
from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO


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

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer_doesnt_exists"
        )

    # Returns all customers list
    def get_all_customers(self) -> list[Customer]:
        return self.customer_repository.get_all()

    # Returns customer
    def get_customer_by_id(self, customer_id: int) -> Customer | None:
        all_customer: list[Customer] = self.customer_repository.get_all()
        one_customer: Customer = self._find_by_id(
            customers_list=all_customer, customer_id=customer_id
        )
        return one_customer

    # Adds customer, creates new ID, returns ID
    def add_customer(self, createCustomerDTO: CreateCustomerDTO) -> int:
        all_customers: list[Customer] = self.customer_repository.get_all()
        for one_customer in all_customers:
            if one_customer.phone_number == createCustomerDTO.phone_number:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Customer_phone_number_already_in_database",
                )
            if one_customer.driver_license_id == createCustomerDTO.driver_license_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Customer_driver_license_already_in_database",
                )

        self.customer_repository.generalId += 1
        new_id: int = self.customer_repository.generalId

        all_customers.append(
            Customer(
                id=new_id,
                name=createCustomerDTO.name,
                lastName=createCustomerDTO.last_name,
                phoneNumber=createCustomerDTO.phone_number,
                driverLicenseId=createCustomerDTO.driver_license_id,
                status=CustomerStatusEnum.UNLOCKED,
            )
        )

        self.customer_repository.save_all(customers_list=all_customers)
        return new_id

    # Deletes customer, returns ID
    def delete_customer(self, customer_id: int) -> int:
        all_customers: list[Customer] = self.customer_repository.get_all()
        self._find_by_id(customers_list=all_customers, customer_id=customer_id)

        all_customers: list[Customer] = [
            one_customer
            for one_customer in all_customers
            if one_customer.id != customer_id
        ]
        self.customer_repository.save_all(customers_list=all_customers)
        return customer_id

    # Updates customer, returns ID
    def update_customer(
        self, customer_id: int, updateCustomerDTO: UpdateCustomerDTO
    ) -> int:
        all_customers: list[Customer] = self.customer_repository.get_all()
        one_customer: Customer = self._find_by_id(
            customers_list=all_customers, customer_id=customer_id
        )
        for c in all_customers:
            if c.phone_number == updateCustomerDTO.phone_number and c.id != customer_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Customer_phone_number_already_in_database",
                )

            if (
                c.driver_license_id == updateCustomerDTO.driver_license_id
                and c.id != customer_id
            ):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Customer_driver_license_already_in_database",
                )

        one_customer.name = updateCustomerDTO.name
        one_customer.last_name = updateCustomerDTO.last_name
        one_customer.phone_number = updateCustomerDTO.phone_number
        one_customer.driver_license_id = updateCustomerDTO.driver_license_id

        self.customer_repository.save_all(customers_list=all_customers)
        return customer_id

    # Blocks customer, returns ID
    def block_customer(self, customer_id: int) -> int:
        all_customers: list[Customer] = self.customer_repository.get_all()
        one_customer: Customer = self._find_by_id(
            customers_list=all_customers, customer_id=customer_id
        )

        if one_customer.status != CustomerStatusEnum.BLOCKED:
            one_customer.status = CustomerStatusEnum.BLOCKED
            self.customer_repository.save_all(customers_list=all_customers)
            return customer_id

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="customer_already_blocked!"
        )

    # Unlocks customer, returns ID
    def unlock_customer(self, customer_id: int) -> int:
        all_customers: list[Customer] = self.customer_repository.get_all()
        one_customer: Customer = self._find_by_id(all_customers, customer_id)

        if one_customer.status != CustomerStatusEnum.UNLOCKED:
            one_customer.status = CustomerStatusEnum.UNLOCKED
            self.customer_repository.save_all(customers_list=all_customers)
            return customer_id

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="customer_wasnt_blocked"
        )
