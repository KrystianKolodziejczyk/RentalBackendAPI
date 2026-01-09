from pydantic import BaseModel


class BlockCustomerResponse(BaseModel):
    blocked_customer_with_id: int
