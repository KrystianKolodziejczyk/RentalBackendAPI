from pydantic import BaseModel


class UpdateCarResponse(BaseModel):
    updated_car_id: int
