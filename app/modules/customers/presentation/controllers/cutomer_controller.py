from fastapi import APIRouter, Depends, status

from app.core.container import get_customer_service
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO
from app.modules.customers.presentation.response import (
    BlockCustomerResponse,
    CreateCustomerResponse,
    DeleteCustomerResponse,
    GetCustomerResponse,
    UnlockCustomerResponse,
    UpdateCustomerResponse,
)

router = APIRouter()

# ===== Rental Controller =======

# ===============================


@router.get(
    "/customers",
    status_code=status.HTTP_200_OK,
    response_model=list[GetCustomerResponse],
)
async def get_all_customers(
    customer_service: ICustomerService = Depends(get_customer_service),
) -> list[GetCustomerResponse]:
    return await customer_service.get_all_customers()


# ===============================


@router.get(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCustomerResponse,
)
async def get_customer_by_id(
    customer_id: int,
    customer_service: ICustomerService = Depends(get_customer_service),
) -> GetCustomerResponse:
    return await customer_service.get_customer_by_id(customer_id)


# ===============================


@router.post(
    "/customers",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCustomerResponse,
)
async def add_customer(
    create_customer_dto: CreateCustomerDTO,
    customer_service: ICustomerService = Depends(get_customer_service),
) -> dict[str, int]:
    new_id: int = await customer_service.add_customer(
        create_customer_dto=create_customer_dto
    )
    return {"created_customer_id": new_id}


# ===============================


@router.delete(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=DeleteCustomerResponse,
)
async def delete_customer(
    customer_id: int, customer_service: ICustomerService = Depends(get_customer_service)
) -> dict[str, int]:
    delete_id: int = await customer_service.delete_customer(customer_id=customer_id)
    return {"deleted_customer_id": delete_id}


# ===============================


@router.put(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=UpdateCustomerResponse,
)
async def update_customer(
    customer_id: int,
    update_customer_dto: UpdateCustomerDTO,
    customer_service: ICustomerService = Depends(get_customer_service),
) -> dict[str, int]:
    updated_id: int = await customer_service.update_customer(
        customer_id=customer_id, update_customer_dto=update_customer_dto
    )
    return {"updated_customer_id": updated_id}


# ===============================


@router.patch(
    "/customers/block/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=BlockCustomerResponse,
)
async def block_customer(
    customer_id: int, customer_service: ICustomerService = Depends(get_customer_service)
) -> dict[str, int]:
    blocked_id: int = await customer_service.block_customer(customer_id=customer_id)
    return {"blocked_customer_with_id": blocked_id}


# ===============================


@router.patch(
    "/customers/unlock/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=UnlockCustomerResponse,
)
async def unlock_customer(
    customer_id: int, customer_service: ICustomerService = Depends(get_customer_service)
) -> dict[str, int]:
    unlock_id: int = await customer_service.unlock_customer(customer_id=customer_id)
    return {"unlocked_customer_with_id": unlock_id}
