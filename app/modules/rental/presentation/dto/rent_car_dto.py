from pydantic import BaseModel


class RentCarDto(BaseModel):
    customer_id: int
    car_id: int
    start_date: str
    planned_end_date: str
