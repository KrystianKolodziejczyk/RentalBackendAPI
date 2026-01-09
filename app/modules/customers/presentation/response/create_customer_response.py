from pydantic import BaseModel


class CreateCustomerResponse(BaseModel):
    created_customer_id: int
