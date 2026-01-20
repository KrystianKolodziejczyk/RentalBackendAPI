from pydantic import BaseModel


class CheckAvailableCarResponse(BaseModel):
    car_status: str
