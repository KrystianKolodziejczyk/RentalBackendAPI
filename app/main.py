from fastapi import FastAPI

app = FastAPI()


@app.get("/api/items")
async def get_all_items(available: int | None = None, rented: int | None = None):
    pass


@app.get("/api/items/{item_id}")
async def get_one_item(item_id: int):
    pass


@app.post("api/items")
async def create_item():
    pass


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
class StoreItem(
    Car
):  # Klasa z której tworzone są instancje samochodów + w której przypisywane jest ID do każdego utworzonego auta
    __id: int

    def __init__(self, brand: str, model: str, year: int, id: int) -> None:
        super().__init__(brand=brand, model=model, year=year)
        self.__id = id

    @property
    def id(self):
        return self.__id


# Storehouse Class
class Storehouse:
    possesedCars: list[
        StoreItem
    ]  # qty danego auta byłoby wyliczane w Storehouse na podstawie ilości wystąpien w StoreItem -- użyj metody listy count

    def __init__(self) -> None:
        self.possesedCars = (
            []
        )  # (pojedyncza) instancja storehouse miałaby atrybut listy ze wszystkimi instancjami StoreItem (dziedziczącej po Car)

    def calculate_each_car_qty(
        self,
    ):  # UWAGA - najprawdopodobniej wyliczane i zwracane w handlerze, formatowane do listy JSONów poprzez respoonse model!!!
        pass


"""
    def available_cars(
        self,
    ) -> list[
        StoreItem
    ]:  # Get all zwracałoby mi listę "marka|model + qty" -- bez ID (otrzymane przy pomocy ResponseModelu ==> return liste Carsów i response model typu response model)
        pass
"""


class Rented:
    def __init__(
        self, id: int, status: str
    ):  # Każda jedna instancja będzie wypożyczonym samochodem -- wypożyczenie będzie modyfikowało "qty" konkretnego modelu, a status wypożyczenia będzie względem ID, a nie modelu
        self.id = id
        self.status = status
