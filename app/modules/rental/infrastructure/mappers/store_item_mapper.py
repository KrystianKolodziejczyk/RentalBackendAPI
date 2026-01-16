from app.modules.rental.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.models.store_item import StoreItem


class StoreItemMapper:
    @staticmethod
    def json_to_storeItem(storeItemDict: dict) -> StoreItem:
        return StoreItem(
            car=Car(
                id=storeItemDict["car"]["id"],
                brand=storeItemDict["car"]["brand"],
                model=storeItemDict["car"]["model"],
                year=storeItemDict["car"]["year"],
            ),
            status=RentStatusEnum(storeItemDict["status"]),
        )

    @staticmethod
    def storeItem_to_json(storeItem: StoreItem) -> dict[str, dict | str]:
        return {
            "car": {
                "id": storeItem.car.id,
                "brand": storeItem.car.brand,
                "model": storeItem.car.model,
                "year": storeItem.car.year,
            },
            "status": storeItem.status.value,
        }
