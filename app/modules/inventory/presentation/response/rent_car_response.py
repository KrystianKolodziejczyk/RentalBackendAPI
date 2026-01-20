from pydantic import BaseModel


class RentCarResponse(BaseModel):
    car_status_changed_to: str
