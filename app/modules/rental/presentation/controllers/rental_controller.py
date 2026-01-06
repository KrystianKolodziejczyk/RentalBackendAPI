from fastapi import FastAPI, status
from app.modules.rental.application.services.rental_service import RentalService
from app.modules.rental.domain.models.car import Car
from app.modules.rental.presentation.dto.create_car_dto import CreateCarDTO
from app.modules.rental.presentation.response.check_available_car_response import (
    CheckAvailableCarResponse,
)
from app.modules.rental.presentation.response.create_car_response import (
    CreateCarResponse,
)
from app.modules.rental.presentation.response.get_car_response import GetCarResponse
from app.modules.rental.infrastructure.repositories.rental_repository import (
    RentalRepository,
)
from app.modules.rental.presentation.response.cars_qty_response import CarsQtyResponse
from app.modules.rental.presentation.response.delete_car_response import (
    DeletCarResponse,
)
from app.modules.rental.presentation.response.rent_car_response import RentCarResponse

rentalRepository = RentalRepository()
rentalService = RentalService(rental_repository=rentalRepository)

app = FastAPI()

# ===== Store Controller ========

# ===============================


@app.get(
    "/api/cars/all", status_code=status.HTTP_200_OK, response_model=list[GetCarResponse]
)
async def get_all_cars() -> list[Car]:
    return rentalService.get_all_cars()


# ===============================


@app.get(
    "/api/cars/all/count",
    status_code=status.HTTP_200_OK,
    response_model=CarsQtyResponse,
)
async def get_all_cars_qty() -> dict[str, int]:
    allCarsQty: int = rentalService.get_all_cars_qty()
    return {"total_number_of_cars": allCarsQty}


# ===============================


@app.get(
    "/api/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCarResponse,
)
async def get_one_car(car_id: int) -> Car:
    return rentalService.get_car_by_id(car_id)


# ===============================


@app.post(
    "/api/cars/all",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCarResponse,
)
async def add_new_car(carDTO: CreateCarDTO) -> dict[str, int]:
    NewCarId: int = rentalService.add_car(carDTO)
    return {"created_car_id": NewCarId}


# ===============================


@app.delete(
    "/api/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=DeletCarResponse,
)
async def delete_car(car_id: int):
    deleteCarId: int = rentalService.delete_car(car_id)
    return {"deleted_car_id": deleteCarId}


# ===============================


@app.get(
    "/api/cars/rented",
    status_code=status.HTTP_200_OK,
    response_model=list[GetCarResponse],
)
async def get_available_cars() -> list[Car]:
    return rentalService.get_available_cars()


# ==============================


@app.get(
    "/api/cars/rented/check/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=CheckAvailableCarResponse,
)
async def check_available_car(car_id: int) -> dict[str, str]:
    carStatus: str = rentalService.check_car_availability(car_id=car_id)
    return {"car_status": carStatus}


# ==============================


@app.patch(
    "/api/cars/rented/rent/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=RentCarResponse,
)
async def rent_car(car_id: int) -> dict[str, str]:
    carStatus: str = rentalService.rent_car(car_id=car_id)
    return {"car_status_changed_to": carStatus}


# ==============================


@app.patch(
    "/api/cars/rented/return/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=RentCarResponse,
)
async def return_car(car_id: int) -> dict[str, str]:
    carStatus: str = rentalService.return_car(car_id=car_id)
    return {"car_status_changed_to": carStatus}
