from fastapi import HTTPException, status

# ===== Exceptions ======


class CarNotFoundException(HTTPException):
    def __init__(self, car_id: int):
        self.car_id = car_id
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Car {car_id} not found"
        )


# =======================


class CarAlreadyRentedException(HTTPException):
    def __init__(self, car_id: int, action: str):
        self.car_id = car_id
        self.action = action
        super().__init__(
            status_code=status.HTTP_409_CONFLICT, detail=f"Cant {action} rented car"
        )


# =======================


class CarIsNotRentedException(HTTPException):
    def __init__(self, car_id: int):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Car {car_id} cant be returned when is not rented",
        )
