from pydantic import BaseModel


class DeletCarResponse(BaseModel):
    deleted_car_id: int
