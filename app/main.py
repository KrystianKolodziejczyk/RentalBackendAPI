from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Cars class - stworzone na poczet symbolicznego rozdzielenia odpowiedzialności
class Car:
    brand: str
    model: str
    year: int

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year


# Store Item class
# Klasa z której tworzone są instancje samochodów + w której przypisywane jest ID do każdego utworzonego auta
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
    # qty danego auta byłoby wyliczane w Storehouse na podstawie ilości wystąpien w StoreItem -- użyj metody listy count
    possesedCars: list

    # (pojedyncza) instancja storehouse miałaby atrybut listy ze wszystkimi instancjami StoreItem (dziedziczącej po Car)
    def __init__(self) -> None:
        self.possesedCars = []

    # UWAGA - najprawdopodobniej wyliczane i zwracane w handlerze, formatowane do listy JSONów poprzez respoonse model!!!
    def calculate_each_car_qty(self):
        pass


class Rented:
    # Każda jedna instancja będzie wypożyczonym samochodem -- wypożyczenie będzie modyfikowało "qty" konkretnego modelu, a status wypożyczenia będzie względem ID, a nie modelu
    def __init__(self, id: int, status: str):
        self.id = id
        self.status = status


class GetCarResponse(BaseModel):
    brand: str
    model: str
    year: int  # Tu był błąd - pamiętaj na zawsze żeby sprawdzać
    id: int


storehouse = Storehouse()

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


@app.get("/api/cars", status_code=200, response_model=list[GetCarResponse])
async def get_all_cars() -> list[StoreItem]:
    return storehouse.possesedCars


@app.get("/api/cars/{car_id}", status_code=200, response_model=GetCarResponse)
async def get_one_car(car_id: int):
    for car in storehouse.possesedCars:
        if car.id == car_id:
            return car


@app.post("/api/cars")
async def add_new_car():
    pass


@app.delete("/api/cars")
async def delete_car():
    pass
