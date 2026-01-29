from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.exceptions.customer_exceptions import (
    CustomerAlreadyBlockedException,
    CustomerAlreadyUnlockedException,
)


class Customer:
    id: int
    name: str
    last_name: str
    phone_number: int
    driver_license_id: str
    status: CustomerStatusEnum

    def __init__(
        self,
        id: int,
        name: str,
        last_name: str,
        phone_number: str,
        status: CustomerStatusEnum,
        driver_license_id: str,
    ) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.driver_license_id = driver_license_id
        self.status = status

    @classmethod
    def create(
        cls,
        name: str,
        last_name: str,
        phone_number: str,
        driver_license_id: str,
    ) -> "Customer":
        return cls(
            id=None,
            name=name,
            last_name=last_name,
            phone_number=phone_number,
            driver_license_id=driver_license_id,
            status=CustomerStatusEnum.UNLOCKED,
        )

    def update(
        self, name: str, last_name: str, phone_number: str, driver_license_id: str
    ) -> None:
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.driver_license_id = driver_license_id

    def block(self) -> None:
        if self.status == CustomerStatusEnum.BLOCKED:
            raise CustomerAlreadyBlockedException(self.id)

        self.status = CustomerStatusEnum.BLOCKED

    def unlock(self) -> None:
        if self.status == CustomerStatusEnum.UNLOCKED:
            raise CustomerAlreadyUnlockedException(self.id)

        self.status = CustomerStatusEnum.UNLOCKED

    def ensure_can_be_deleted(self) -> None:
        if self.status == CustomerStatusEnum.BLOCKED:
            raise CustomerAlreadyBlockedException(self.id)
