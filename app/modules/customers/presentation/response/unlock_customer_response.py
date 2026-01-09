from pydantic import BaseModel


class UnlockCustomerResponse(BaseModel):
    unlocked_customer_with_id: int
