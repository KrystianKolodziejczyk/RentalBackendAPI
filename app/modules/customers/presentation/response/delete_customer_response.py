from pydantic import BaseModel


class DeleteCustomerResponse(BaseModel):
    deleted_customer_id: int
