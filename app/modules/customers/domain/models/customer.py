from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum


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
        lastName: str,
        phoneNumber: int,
        status: CustomerStatusEnum,
        driverLicenseId: str,
    ) -> None:
        self.id = id
        self.name = name
        self.last_name = lastName
        self.phone_number = phoneNumber
        self.driver_license_id = driverLicenseId
        self.status: CustomerStatusEnum = status
