from pydantic import BaseModel


class UpdateCustomerResponse(BaseModel):
    updated_customer_id: int
