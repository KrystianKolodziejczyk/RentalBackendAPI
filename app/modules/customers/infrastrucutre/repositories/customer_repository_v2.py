from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.shared.infrastructure.services.fake_database.fake_database import FakeDatabse
from app.modules.customers.infrastrucutre.mappers.customer_mapper import CustomerMapper
from pathlib import Path


class CustomerRepositoryV2(ICustomerRepository):
    path: Path

    def __init__(self, path: Path):
        self.path = path

    def get_all(self) -> list[Customer]:
        customers_list_dict: list[dict] = FakeDatabse.get_json_list(path=self.path)
        return [
            CustomerMapper.json_to_customer(customer_dict=one_customer)
            for one_customer in customers_list_dict
        ]

    def save_all(self, customers_list: list[Customer]) -> None:
        customers_list_dict: list[dict] = [
            CustomerMapper.customer_to_json(one_customer)
            for one_customer in customers_list
        ]

        FakeDatabse.save_json_list(path=self.path, python_data=customers_list_dict)
