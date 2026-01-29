from aiosqlite import IntegrityError

from app.modules.customers.domain.exceptions.customer_exceptions import (
    DriverLicenseInDatabaseException,
    PhoneNumberInDatabaseException,
)
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.infrastructure.mappers.customer_mapper import CustomerMapper
from app.shared.domain.services.i_sqlite_client.i_sqlite_client import ISqliteClient


class CustomerRepository(ICustomerRepository):
    _db_client: ISqliteClient

    def __init__(self, db_client: ISqliteClient):
        self._db_client = db_client

    # Helper
    def _return_exception(self, exception: IntegrityError, customer_dict: dict) -> None:
        error_message: str = str(exception).lower()

        if "phone_number" in error_message:
            raise PhoneNumberInDatabaseException(
                phone_number=customer_dict["phone_number"]
            )

        elif "driver_license_id" in error_message:
            raise DriverLicenseInDatabaseException(
                driver_license_id=customer_dict["driver_license_id"]
            )

        else:
            raise IntegrityError(f"Database constraint violation: {exception}")

    # Gets one customer
    async def get_customer_by_id(self, customer_id: int) -> Customer:
        query: str = """
        SELECT * FROM customers WHERE id = ?;
        """
        customer_dict: dict = await self._db_client.fetch_one(
            query=query, params=(customer_id,)
        )
        if not customer_dict:
            return None

        return CustomerMapper.dict_to_customer(customer_dict=customer_dict)

    # Gets all customers
    async def get_all_customers(self) -> list[Customer]:
        query: str = """
        SELECT * FROM customers;
        """
        list_dict_customers: list[Customer] = await self._db_client.fetch_all(
            query=query
        )

        return [
            CustomerMapper.dict_to_customer(one_customer)
            for one_customer in list_dict_customers
        ]

    # Adds new customer
    async def add_customer(self, customer: Customer) -> int:
        customer_dict: dict = CustomerMapper.customer_to_dict(customer=customer)
        query: str = """
        INSERT INTO customers (name, last_name, phone_number, driver_license_id, status)
        VALUES (?, ?, ?, ?, ?);
        """

        try:
            new_id: int = await self._db_client.execute(
                query=query,
                params=(
                    customer_dict["name"],
                    customer_dict["last_name"],
                    customer_dict["phone_number"],
                    customer_dict["driver_license_id"],
                    customer_dict["status"],
                ),
            )

            return new_id

        except IntegrityError as e:
            self._return_exception(exception=e, customer_dict=customer_dict)

    # Deletes customer
    async def delete_customer(self, customer_id: int) -> int:
        query: str = "DELETE FROM customers WHERE id = ?"
        await self._db_client.execute(query=query, params=(customer_id,))

        return customer_id

    # Updates customer
    async def update_customer(self, customer_id: int, customer: Customer) -> int:
        customer_dict: dict = CustomerMapper.customer_to_dict(customer=customer)
        query: str = """
        UPDATE customers
        SET name = ?,
        last_name = ?,
        phone_number = ?,
        driver_license_id = ?
        WHERE id = ?;
        """

        try:
            await self._db_client.execute(
                query=query,
                params=(
                    customer_dict["name"],
                    customer_dict["last_name"],
                    customer_dict["phone_number"],
                    customer_dict["driver_license_id"],
                    customer_id,
                ),
            )
            return customer_id

        except IntegrityError as e:
            self._return_exception(exception=e, customer_dict=customer_dict)

    # Changes customer status
    async def change_status_customer(self, customer_id: int, new_status: str) -> int:
        query: str = """
        UPDATE customers
        SET status = ?
        WHERE id = ?;
        """

        await self._db_client.execute(query=query, params=(new_status, customer_id))

        return customer_id
