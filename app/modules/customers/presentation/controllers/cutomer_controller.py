from fastapi import APIRouter, status, Depends

from app.core.container import get_customer_service
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.dto import CreateCustomerDTO, UpdateCustomerDTO
from app.modules.customers.presentation.response import (
    GetCustomerResponse,
    CreateCustomerResponse,
    UpdateCustomerResponse,
    BlockCustomerResponse,
    UnlockCustomerResponse,
    DeleteCustomerResponse,
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
    customerService: ICustomerService = Depends(get_customer_service),
) -> list[GetCustomerResponse]:
    return customerService.get_all_customers()


# ===============================


@router.get(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCustomerResponse,
)
async def get_customer_by_id(
    customer_id: int,
    customerService: ICustomerService = Depends(get_customer_service),
) -> GetCustomerResponse:
    return customerService.get_customer_by_id(customer_id)


# ===============================


@router.post(
    "/customers",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCustomerResponse,
)
async def add_customer(
    createCustomerDTO: CreateCustomerDTO,
    customerService: ICustomerService = Depends(get_customer_service),
) -> dict[str, int]:
    newId: int = customerService.add_customer(createCustomerDTO=createCustomerDTO)
    return {"created_customer_id": newId}


# ===============================


@router.delete(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=DeleteCustomerResponse,
)
async def delete_customer(
    customer_id: int, customerService: ICustomerService = Depends(get_customer_service)
):
    deleteId: int = customerService.delete_customer(customer_id=customer_id)
    return {"deleted_customer_id": deleteId}


# ===============================


@router.put(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=UpdateCustomerResponse,
)
async def update_customer(
    customer_id: int,
    updateCustomerDTO: UpdateCustomerDTO,
    customerService: ICustomerService = Depends(get_customer_service),
) -> dict[str, int]:
    updatedId: int = customerService.update_customer(
        customer_id=customer_id, updateCustomerDTO=updateCustomerDTO
    )
    return {"updated_customer_id": updatedId}


# ===============================


@router.patch(
    "/customers/block/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=BlockCustomerResponse,
)
async def block_customer(
    customer_id: int, customerService: ICustomerService = Depends(get_customer_service)
) -> dict[str, int]:
    blockedId: int = customerService.block_customer(customer_id=customer_id)
    return {"blocked_customer_with_id": blockedId}


# ===============================


@router.patch(
    "/customers/unlock/{customer_id}",
    status_code=status.HTTP_200_OK,
    response_model=UnlockCustomerResponse,
)
async def unlock_customer(
    customer_id: int, customerService: ICustomerService = Depends(get_customer_service)
) -> dict[str, int]:
    unlockId: int = customerService.unlock_customer(customer_id=customer_id)
    return {"unlocked_customer_with_id": unlockId}
