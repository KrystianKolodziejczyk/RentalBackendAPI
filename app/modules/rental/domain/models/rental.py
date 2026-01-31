from datetime import datetime, timezone

from app.modules.rental.domain.rental_exceptions.rental_exceptions import (
    RentalAlreadyReturnedException,
)


class Rental:
    id: int
    customer_id: int
    car_id: int
    start_date: str
    planned_end_date: str
    actual_end_date: str | None
    created_at: str | None

    def __init__(
        self,
        id: int,
        customer_id: int,
        car_id: int,
        start_date: str,
        planned_end_date: str,
        actual_end_date: str | None,
        created_at: str | None,
    ) -> None:
        self.id = id
        self.customer_id = customer_id
        self.car_id = car_id
        self.start_date = start_date
        self.planned_end_date = planned_end_date
        self.actual_end_date = actual_end_date
        self.created_at = created_at

    @classmethod
    def create(
        cls,
        customer_id: int,
        car_id: int,
        start_date: str,
        planned_end_date: str,
        actual_end_date: str | None = None,
    ) -> "Rental":
        return cls(
            id=None,
            customer_id=customer_id,
            car_id=car_id,
            start_date=start_date,
            planned_end_date=planned_end_date,
            actual_end_date=actual_end_date,
            created_at=None,
        )

    def complete_return(self) -> None:
        if self.actual_end_date is not None:
            raise RentalAlreadyReturnedException(self.id)

        self.actual_end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
