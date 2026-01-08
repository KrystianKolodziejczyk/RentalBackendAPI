from fastapi import APIRouter


router = APIRouter()


@router.get("/customers")
async def get_all_customers():
    pass


@router.get("/customers/{customer_id}")
async def get_one_customer(customer_id: int):
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
