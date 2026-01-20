from pydantic import BaseModel


# Get response schema
class GetCarResponse(BaseModel):
    brand: str
    model: str
    year: int
    id: int
