from fastapi import APIRouter, status, Depends

from app.core.container import get_rental_service
from app.modules.rental.domain.models.car import Car
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.presentation.dto import CreateCarDTO, UpdateCarDTO
from app.modules.rental.presentation.response import (
    CreateCarResponse,
    CheckAvailableCarResponse,
    CarsQtyResponse,
    DeleteCarResponse,
    GetCarResponse,
    RentCarResponse,
    UpdateCarResponse,
)


router = APIRouter()

# ===== Rental Controller ========

# ===============================


@router.get(
    "/cars/all", status_code=status.HTTP_200_OK, response_model=list[GetCarResponse]
)
async def get_all_cars(
    rentalService: IRentalService = Depends(get_rental_service),
) -> list[Car]:
    return rentalService.get_all_cars()


# ===============================


@router.get(
    "/cars/all/count",
    status_code=status.HTTP_200_OK,
    response_model=CarsQtyResponse,
)
async def get_all_cars_qty(
    rentalService: IRentalService = Depends(get_rental_service),
) -> dict[str, int]:
    allCarsQty: int = rentalService.get_all_cars_qty()
    return {"total_number_of_cars": allCarsQty}


# ===============================


@router.get(
    "/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCarResponse,
)
async def get_one_car(
    car_id: int, rentalService: IRentalService = Depends(get_rental_service)
) -> Car:
    return rentalService.get_car_by_id(car_id)


# ===============================


@router.post(
    "/cars/all",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCarResponse,
)
async def add_new_car(
    createCarDTO: CreateCarDTO,
    rentalService: IRentalService = Depends(get_rental_service),
) -> dict[str, int]:
    NewCarId: int = rentalService.add_car(createCarDTO=createCarDTO)
    return {"created_car_id": NewCarId}


# ===============================


@router.delete(
    "/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=DeleteCarResponse,
)
async def delete_car(
    car_id: int, rentalService: IRentalService = Depends(get_rental_service)
) -> dict[str, int]:
    deleteCarId: int = rentalService.delete_car(car_id)
    return {"deleted_car_id": deleteCarId}


# ===============================


@router.put(
    "/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=UpdateCarResponse,
)
async def update_car(
    car_id: int,
    updateCarDTO: UpdateCarDTO,
    rentalService: IRentalService = Depends(get_rental_service),
) -> dict[str, int]:
    updateCarId: int = rentalService.update_car(
        car_id=car_id, updateCarDTO=updateCarDTO
    )
    return {"updated_car_id": updateCarId}


# ===============================


@router.get(
    "/cars/rented",
    status_code=status.HTTP_200_OK,
    response_model=list[GetCarResponse],
)
async def get_available_cars(
    rentalService: IRentalService = Depends(get_rental_service),
) -> list[Car]:
    return rentalService.get_available_cars()


# ==============================


@router.get(
    "/cars/rented/check/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=CheckAvailableCarResponse,
)
async def check_available_car(
    car_id: int, rentalService: IRentalService = Depends(get_rental_service)
) -> dict[str, str]:
    carStatus: str = rentalService.check_car_availability(car_id=car_id)
    return {"car_status": carStatus}


# ==============================


@router.patch(
    "/cars/rented/rent/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=RentCarResponse,
)
async def rent_car(
    car_id: int, rentalService: IRentalService = Depends(get_rental_service)
) -> dict[str, str]:
    carStatus: str = rentalService.rent_car(car_id=car_id)
    return {"car_status_changed_to": carStatus}


# ==============================


@router.patch(
    "/cars/rented/return/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=RentCarResponse,
)
async def return_car(
    car_id: int, rentalService: IRentalService = Depends(get_rental_service)
) -> dict[str, str]:
    carStatus: str = rentalService.return_car(car_id=car_id)
    return {"car_status_changed_to": carStatus}
