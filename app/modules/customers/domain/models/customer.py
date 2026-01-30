from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.exceptions.customer_exceptions import (
    CustomerAlreadyBlockedException,
    CustomerAlreadyUnlockedException,
)
from app.modules.customers.domain.value_objects import DriverLicenseId, PhoneNumber


class Customer:
    id: int
    name: str
    last_name: str
    phone_number: PhoneNumber
    driver_license_id: DriverLicenseId
    status: CustomerStatusEnum

    def __init__(
        self,
        id: int,
        name: str,
        last_name: str,
        phone_number: PhoneNumber,
        status: CustomerStatusEnum,
        driver_license_id: DriverLicenseId,
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
        phone_number: PhoneNumber,
        driver_license_id: DriverLicenseId,
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
        self,
        name: str,
        last_name: str,
        phone_number: PhoneNumber,
        driver_license_id: DriverLicenseId,
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

    def ensure_not_blocked(self) -> None:
        if self.status == CustomerStatusEnum.BLOCKED:
            raise CustomerAlreadyBlockedException(self.id)
