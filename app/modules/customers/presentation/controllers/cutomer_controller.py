from fastapi import APIRouter, status, Depends
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.presentation.response import GetCustomerResponse
from app.core.container import get_customer_service


router = APIRouter()


@router.get(
    "/customers",
    status_code=status.HTTP_200_OK,
    response_model=list[GetCustomerResponse],
)
async def get_all_customers(
    customerService: ICustomerService = Depends(get_customer_service),
) -> list[GetCustomerResponse]:
    return customerService.get_all_customers()


@router.get("/customers/{customer_id}")
async def get_customer_by_id(customer_id: int):
    pass


@router.post("/customers")
async def add_customer():
    pass


@router.put("/customers/{customer_id}")
async def update_customer(customer_id: int):
    pass


@router.patch("/customers/block/{customer_id}")
async def block_customer(customer_id: int):
    pass


@router.patch("/customers/unlock/{customer_id}")
async def unlock_customer(customer_id: int):
    pass
