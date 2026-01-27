from pydantic import BaseModel


class GetCustomerResponse(BaseModel):
    id: int
    name: str
    last_name: str
    phone_number: str
    driver_license_id: str
    status: str
