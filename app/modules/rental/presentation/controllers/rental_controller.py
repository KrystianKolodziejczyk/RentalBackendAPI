from fastapi import APIRouter, Depends, status

from app.core.container import get_rental_service
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.presentation.dto import RentCarDto
from app.modules.rental.presentation.responses import (
    GetRentalResponse,
    RentCarResponse,
    ReturnCarResponse,
)

router = APIRouter()

# ===== Rental Controller ======


# ==============================


@router.get(
    "/rental", status_code=status.HTTP_200_OK, response_model=list[GetRentalResponse]
)
async def get_all_rental(
    rental_service: IRentalService = Depends(get_rental_service),
) -> list[GetRentalResponse]:
    return await rental_service.get_all_rentals()


# ==============================


@router.post(
    "/rental/rent", status_code=status.HTTP_201_CREATED, response_model=RentCarResponse
)
async def rent_car(
    rent_car_dto: RentCarDto,
    rental_service: IRentalService = Depends(get_rental_service),
) -> dict[str, int]:
    rented_car_id: int = await rental_service.rent_car(rent_car_dto=rent_car_dto)
    return {"rented_car_with_id": rented_car_id}


# ==============================


@router.patch(
    "/rental/return/{rental_id}",
    status_code=status.HTTP_200_OK,
    response_model=ReturnCarResponse,
)
async def return_car(
    rental_id: int,
    rental_service: IRentalService = Depends(get_rental_service),
) -> dict[str, int]:
    return_car_id: int = await rental_service.return_car(rental_id=rental_id)
    return {"returned_car_id": return_car_id}


# ==============================


@router.get(
    "/rental/{rental_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetRentalResponse,
)
async def get_rental_by_id(
    rental_id: int, rental_service: IRentalService = Depends(get_rental_service)
) -> GetRentalResponse:
    return await rental_service.get_rental_by_id(rental_id=rental_id)
