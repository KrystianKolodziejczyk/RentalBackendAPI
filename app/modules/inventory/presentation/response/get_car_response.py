from pydantic import BaseModel

from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum


class GetCarResponse(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    status: RentStatusEnum
