from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.models.store_item import StoreItem


class StoreItemMapper:
    @staticmethod
    def json_to_store_item(store_item_dict: dict) -> StoreItem:
        return StoreItem(
            car=Car(
                id=store_item_dict["car"]["id"],
                brand=store_item_dict["car"]["brand"],
                model=store_item_dict["car"]["model"],
                year=store_item_dict["car"]["year"],
            ),
            status=RentStatusEnum(store_item_dict["status"]),
        )

    @staticmethod
    def store_item_to_json(store_item: StoreItem) -> dict[str, dict | str]:
        return {
            "car": {
                "id": store_item.car.id,
                "brand": store_item.car.brand,
                "model": store_item.car.model,
                "year": store_item.car.year,
            },
            "status": store_item.status.value,
        }
