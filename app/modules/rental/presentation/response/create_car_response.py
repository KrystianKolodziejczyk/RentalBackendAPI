from pydantic import BaseModel


# Response schema
class CreateCarResponse(BaseModel):
    created_car_id: int
