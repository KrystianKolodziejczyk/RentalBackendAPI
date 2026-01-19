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
        last_name: str,
        phone_number: int,
        status: CustomerStatusEnum,
        driver_license_id: str,
    ) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.driver_license_id = driver_license_id
        self.status = status
