from pydantic import BaseModel


class RentCarResponse(BaseModel):
    rented_car_with_id: int
