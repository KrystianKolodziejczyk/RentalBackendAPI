from pydantic import BaseModel


class GetRentalResponse(BaseModel):
    id: int
    customer_id: int
    car_id: int
    start_date: str
    planned_end_date: str
    actual_end_date: str | None
    created_at: str
