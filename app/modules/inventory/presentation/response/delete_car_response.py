from pydantic import BaseModel


class DeleteCarResponse(BaseModel):
    deleted_car_id: int
