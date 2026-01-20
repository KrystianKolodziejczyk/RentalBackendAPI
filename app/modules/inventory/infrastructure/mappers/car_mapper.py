from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.inventory.domain.models.car import Car


class CarMapper:
    @staticmethod
    def json_to_car(car_dict: dict) -> Car:
        return Car(
            id=car_dict["id"],
            brand=car_dict["brand"],
            model=car_dict["model"],
            year=car_dict["year"],
            status=RentStatusEnum(car_dict["status"]),
        )

    @staticmethod
    def car_to_json(car: Car) -> dict[str, str | int]:
        return {
            "id": car.id,
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "status": car.status.value,
        }
