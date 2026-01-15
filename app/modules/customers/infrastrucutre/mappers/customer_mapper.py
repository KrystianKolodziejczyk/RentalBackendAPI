from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.enums.customer_status_enum import CustomerStatusEnum


class CustomerMapper:
    @staticmethod
    def json_to_customer(customerDict: dict) -> Customer:
        return Customer(
            id=customerDict["id"],
            name=customerDict["name"],
            lastName=customerDict["last_name"],
            phoneNumber=customerDict["phone_number"],
            driverLicenseId=customerDict["driver_license_id"],
            status=CustomerStatusEnum(customerDict["status"]),
        )

    @staticmethod  # Probably to delete
    def customer_to_json(customer: Customer) -> dict[str, str | int]:
        return {
            "id": customer.id,
            "name": customer.name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number,
            "driver_license_id": customer.driver_license_id,
            "status": customer.status.value,
        }
