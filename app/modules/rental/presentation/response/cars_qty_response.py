from pydantic import BaseModel


class CarsQtyResponse(BaseModel):
    total_number_of_cars: int
