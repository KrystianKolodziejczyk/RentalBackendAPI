from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Cars class
class Car:
    brand: str
    model: str
    year: int

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year


# Store Item class
class StoreItem(Car):
    __id: int

    def __init__(self, brand: str, model: str, year: int, id: int) -> None:
        super().__init__(brand=brand, model=model, year=year)
        self.__id = id

    @property
    def id(self):
        return self.__id


# Storehouse Class
class Storehouse:
    possesedCars: list

    def __init__(self) -> None:
        self.possesedCars = []


# Rentend cars class
class Rented:
    def __init__(self, id: int, status: str):
        self.id = id
        self.status = status


# Get response model
class GetCarResponse(BaseModel):
    brand: str
    model: str
    year: int
    id: int


# Signletone instance
storehouse = Storehouse()

# Fake Database
storehouse.possesedCars = [
    StoreItem(id=1, brand="BMW", model="M3", year=2019),
    StoreItem(id=2, brand="BMW", model="M3", year=2019),
    StoreItem(id=3, brand="BMW", model="M3", year=2019),
    StoreItem(id=4, brand="BMW", model="M3", year=2019),
    StoreItem(id=5, brand="BMW", model="M4", year=2019),
    StoreItem(id=6, brand="BMW", model="M4", year=2019),
    StoreItem(id=7, brand="BMW", model="M4", year=2019),
    StoreItem(id=8, brand="BMW", model="M4", year=2019),
    StoreItem(id=9, brand="Audi", model="RS6", year=2019),
    StoreItem(id=10, brand="Audi", model="RS6", year=2019),
    StoreItem(id=11, brand="Audi", model="RS6", year=2019),
    StoreItem(id=12, brand="Audi", model="RS7", year=2019),
    StoreItem(id=13, brand="Audi", model="RS7", year=2019),
]


# Gets all cars
@app.get("/api/cars", status_code=200, response_model=list[GetCarResponse])
async def get_all_cars() -> list[StoreItem]:
    return storehouse.possesedCars


# Gets one car by ID
@app.get("/api/cars/{car_id}", status_code=200, response_model=GetCarResponse)
async def get_one_car(car_id: int):
    for car in storehouse.possesedCars:
        if car.id == car_id:
            return car


# Adds new car
@app.post("/api/cars")
async def add_new_car():
    pass


# deletes selected car
@app.delete("/api/cars")
async def delete_car():
    pass
