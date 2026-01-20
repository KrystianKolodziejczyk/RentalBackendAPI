from pydantic import BaseModel


class UpdateCarDTO(BaseModel):
    brand: str
    model: str
    year: int
