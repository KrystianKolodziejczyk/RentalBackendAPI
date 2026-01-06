from pydantic import BaseModel


# Car's DTO
class CreateCarDTO(BaseModel):
    brand: str
    model: str
    year: int
