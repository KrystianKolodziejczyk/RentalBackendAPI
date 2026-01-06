from app.modules.rental.domain.models.car import Car
from app.modules.rental.infrastructure.repositories.rental_repository import (
    RentalRepository,
)


# Signletone instance
storehouse = RentalRepository()

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
availableCars = storehouse.get_available

for car in availableCars:
    print(car.car.model)
