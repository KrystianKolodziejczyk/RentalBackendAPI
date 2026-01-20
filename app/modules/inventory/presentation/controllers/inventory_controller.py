from fastapi import APIRouter, status, Depends

from app.core.container import get_inventory_service
from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.services.i_inventory_service import IInventoryService
from app.modules.inventory.presentation.dto import CreateCarDTO, UpdateCarDTO
from app.modules.inventory.presentation.response import (
    CreateCarResponse,
    CheckAvailableCarResponse,
    CarsQtyResponse,
    DeleteCarResponse,
    GetCarResponse,
    RentCarResponse,
    UpdateCarResponse,
)


router = APIRouter()

# ===== Inventory Controller =======

# ===============================


@router.get(
    "/cars/all", status_code=status.HTTP_200_OK, response_model=list[GetCarResponse]
)
async def get_all_cars(
    inventory_service: IInventoryService = Depends(get_inventory_service),
) -> list[GetCarResponse]:
    return inventory_service.get_all_cars()


# ===============================


@router.get(
    "/cars/all/count",
    status_code=status.HTTP_200_OK,
    response_model=CarsQtyResponse,
)
async def get_all_cars_qty(
    inventory_service: IInventoryService = Depends(get_inventory_service),
) -> dict[str, int]:
    all_cars_qty: int = inventory_service.get_all_cars_qty()
    return {"total_number_of_cars": all_cars_qty}


# ===============================


@router.get(
    "/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCarResponse,
)
async def get_one_car(
    car_id: int, inventory_service: IInventoryService = Depends(get_inventory_service)
) -> GetCarResponse:
    return inventory_service.get_car_by_id(car_id)


# ===============================


@router.post(
    "/cars/all",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCarResponse,
)
async def add_new_car(
    create_car_dto: CreateCarDTO,
    inventory_service: IInventoryService = Depends(get_inventory_service),
) -> dict[str, int]:
    new_car_id: int = inventory_service.add_car(create_car_dto=create_car_dto)
    return {"created_car_id": new_car_id}


# ===============================


@router.delete(
    "/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=DeleteCarResponse,
)
async def delete_car(
    car_id: int, inventory_service: IInventoryService = Depends(get_inventory_service)
) -> dict[str, int]:
    delete_car_id: int = inventory_service.delete_car(car_id)
    return {"deleted_car_id": delete_car_id}


# ===============================


@router.put(
    "/cars/all/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=UpdateCarResponse,
)
async def update_car(
    car_id: int,
    update_car_dto: UpdateCarDTO,
    inventory_service: IInventoryService = Depends(get_inventory_service),
) -> dict[str, int]:
    update_car_id: int = inventory_service.update_car(
        car_id=car_id, update_car_dto=update_car_dto
    )
    return {"updated_car_id": update_car_id}


# ===============================


@router.get(
    "/cars/rental/available",
    status_code=status.HTTP_200_OK,
    response_model=list[GetCarResponse],
)
async def get_available_cars(
    inventory_service: IInventoryService = Depends(get_inventory_service),
) -> list[Car]:
    return inventory_service.get_available_cars()


# ==============================


@router.get(
    "/cars/rental/available/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=CheckAvailableCarResponse,
)
async def check_available_car(
    car_id: int, inventory_service: IInventoryService = Depends(get_inventory_service)
) -> dict[str, str]:
    car_status: str = inventory_service.check_car_status(car_id=car_id)
    return {"car_status": car_status}


# ==============================


@router.patch(
    "/cars/rental/rent/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=RentCarResponse,
)
async def rent_car(
    car_id: int, inventory_service: IInventoryService = Depends(get_inventory_service)
) -> dict[str, str]:
    car_status: str = inventory_service.rent_car(car_id=car_id)
    return {"car_status_changed_to": car_status}


# ==============================


@router.patch(
    "/cars/rental/return/{car_id}",
    status_code=status.HTTP_200_OK,
    response_model=RentCarResponse,
)
async def return_car(
    car_id: int, inventory_service: IInventoryService = Depends(get_inventory_service)
) -> dict[str, str]:
    car_status: str = inventory_service.return_car(car_id=car_id)
    return {"car_status_changed_to": car_status}
