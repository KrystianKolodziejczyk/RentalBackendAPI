from pydantic import BaseModel, Field


class CreateCustomerDTO(BaseModel):
    name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    phone_number: int = Field(description="Phone number must have 9 digits")
    driver_license_id: str = Field(
        min_length=16,
        max_length=16,
        description="Drivers Linense must have 16 characters",
    )
