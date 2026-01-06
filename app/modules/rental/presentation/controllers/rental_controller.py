from fastapi import FastAPI
from app.modules.rental.domain.models.store_item import StoreItem
from app.modules.rental.presentation.response.get_car_response import GetCarResponse
from fastapi import status
from app.modules.rental.infrastructure.repositories.rental_repository import (
    RentalRepository,
)

storehouse = RentalRepository()
app = FastAPI()


# Gets all cars
@app.get(
    "/api/cars", status_code=status.HTTP_200_OK, response_model=list[GetCarResponse]
)
async def get_all_cars() -> list[StoreItem]:
    pass


# Gets one car by ID
@app.get(
    "/api/cars/{car_id}", status_code=status.HTTP_200_OK, response_model=GetCarResponse
)
async def get_one_car(car_id: int):
    pass


# Adds new car
@app.post("/api/cars", status_code=status.HTTP_201_CREATED)
async def add_new_car():
    pass


# deletes selected car
@app.delete("/api/cars", status_code=status.HTTP_200_OK)
async def delete_car():
    pass
