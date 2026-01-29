from fastapi import HTTPException, status

# ===== Exceptions ======


class CustomerNotFoundException(HTTPException):
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer {customer_id} not found",
        )


# =======================


class PhoneNumberInDatabaseException(HTTPException):
    def __init__(self, phone_number: int):
        self.phone_number = phone_number
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Phone number: {phone_number} already in database",
        )


# =======================


class DriverLicenseInDatabaseException(HTTPException):
    def __init__(self, driver_license_id: str):
        self.driver_license_id = driver_license_id
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Driver License id: {driver_license_id} already in database",
        )


# =======================


class CustomerAlreadyBlockedException(HTTPException):
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Customer {customer_id} already blocked",
        )


# =======================


class CustomerAlreadyUnlockedException(HTTPException):
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Customer {customer_id} already unlocked",
        )
