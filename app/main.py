from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from enum import Enum

app = FastAPI()


class RentStatus(Enum):
    RENTED = "rented"
    AVAILABLE = "available"


# Cars class
class Car:
    id: str
    brand: str
    model: str
    year: int

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.id = uuid4()


# Rented item class
class StoreItem:
    car: Car
    status: RentStatus

    def __init__(self, car: Car, status: RentStatus):
        self.car = car
        self.status = status


# Storehouse Class
class Storehouse:
    ownedCars: list[StoreItem]

    def __init__(self) -> None:
        self.ownedCars = []

    def add_car(self, car: Car):
        self.ownedCars.append(StoreItem(car=car, status=RentStatus.AVAILABLE))

    @property
    def qty(self):
        return len(self.ownedCars)

    @property
    def get_available(self):
        return [item for item in self.ownedCars if item.status == RentStatus.AVAILABLE]


# Get response model
class GetCarResponse(BaseModel):
    brand: str
    model: str
    year: int
    id: int


# Signletone instance
storehouse = Storehouse()

car1 = Car(brand="BMW", model="M3", year=2022)
car3 = Car(brand="BMW", model="M3", year=2022)
car4 = Car(brand="BMW", model="M3", year=2022)
car6 = Car(brand="BMW", model="M3", year=2022)
car7 = Car(brand="BMW", model="M3", year=2022)
car18 = Car(brand="BMW", model="M3", year=2022)
car9 = Car(brand="BMW", model="M3", year=2022)
storehouse.add_car(car1)
storehouse.add_car(car3)
storehouse.add_car(car4)
storehouse.add_car(car6)
storehouse.add_car(car7)
storehouse.add_car(car18)
storehouse.add_car(car9)
print(storehouse.get_available)


# Gets all cars
@app.get("/api/cars", status_code=200, response_model=list[GetCarResponse])
async def get_all_cars() -> list[StoreItem]:
    pass


# Gets one car by ID
@app.get("/api/cars/{car_id}", status_code=200, response_model=GetCarResponse)
async def get_one_car(car_id: int):
    pass


# Adds new car
@app.post("/api/cars")
async def add_new_car():
    pass


# deletes selected car
@app.delete("/api/cars")
async def delete_car():
    pass
