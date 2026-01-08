from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum


class Customer:
    id: int
    name: str
    lastName: str
    phoneNumber: int
    status: CustomerStatusEnum
    driverLicenseId: str

    def __init__(
        self,
        id: int,
        name: str,
        lastName: str,
        phoneNumber: int,
        status: CustomerStatusEnum,
        driverLicenseId: str,
    ):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.status = status
        self.driverLicenseId = driverLicenseId
