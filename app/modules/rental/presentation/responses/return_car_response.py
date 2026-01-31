from pydantic import BaseModel


class ReturnCarResponse(BaseModel):
    returned_car_id: int
