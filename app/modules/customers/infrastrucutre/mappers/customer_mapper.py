from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum
from app.modules.customers.domain.models.customer import Customer


class CustomerMapper:
    @staticmethod
    def dict_to_customer(customer_dict: dict) -> Customer:
        return Customer(
            id=customer_dict["id"],
            name=customer_dict["name"],
            last_name=customer_dict["last_name"],
            phone_number=customer_dict["phone_number"],
            driver_license_id=customer_dict["driver_license_id"],
            status=CustomerStatusEnum(customer_dict["status"]),
        )

    @staticmethod  # Probably to delete
    def customer_to_dict(customer: Customer) -> dict[str, str | int]:
        return {
            "id": customer.id,
            "name": customer.name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number,
            "driver_license_id": customer.driver_license_id,
            "status": customer.status.value,
        }
