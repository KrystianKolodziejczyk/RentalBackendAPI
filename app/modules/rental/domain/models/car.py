# Car's class
class Car:
    id: str
    brand: str
    model: str
    year: int

    def __init__(self, id: int, brand: str, model: str, year: int) -> None:
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
