class Rental:
    id: int
    customer_id: int
    car_id: int
    start_date: str
    planned_end_date: str
    actual_end_date: str | None
    created_at: str

    def __init__(
        self,
        id: int,
        customer_id: int,
        car_id: int,
        start_date: str,
        planned_end_date: str,
        actual_end_date: str | None,
        created_at: str,
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
        )

    def rent_car(self, customer_id: int, car_id: int) -> None:
        pass

    def return_car(self, customer_id: int, car_id: int) -> None:
        pass
