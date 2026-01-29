from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.value_objects import DriverLicenseId, PhoneNumber


class CustomerMapper:
    @staticmethod
    def dict_to_customer(customer_dict: dict) -> Customer:
        return Customer(
            id=customer_dict["id"],
            name=customer_dict["name"],
            last_name=customer_dict["last_name"],
            phone_number=PhoneNumber(value=customer_dict["phone_number"]),
            driver_license_id=DriverLicenseId(value=customer_dict["driver_license_id"]),
            status=CustomerStatusEnum(customer_dict["status"]),
        )

    @staticmethod
    def customer_to_dict(customer: Customer) -> dict[str, str | int]:
        return {
            "id": customer.id,
            "name": customer.name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number.value,
            "driver_license_id": customer.driver_license_id.value,
            "status": customer.status.value,
        }
