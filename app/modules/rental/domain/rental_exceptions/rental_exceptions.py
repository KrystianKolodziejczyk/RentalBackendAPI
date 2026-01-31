from fastapi import HTTPException, status

# =====================


class RentalNotFoundException(HTTPException):
    def __init__(self, rental_id: int) -> None:
        self.rental_id = rental_id
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rental {rental_id} doesn't exists",
        )


# =====================


class RentalAlreadyReturnedException(HTTPException):
    def __init__(self, rental_id: int) -> None:
        self.rental_id = rental_id
        super().__init__(
            status_code=status.HTTP_409_CONFLICT, detail="Rental already returned"
        )
