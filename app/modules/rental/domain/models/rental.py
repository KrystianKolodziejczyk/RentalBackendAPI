from app.modules.customers.domain.models.customer import Customer
from app.modules.inventory.domain.models.car import Car


class Rental:
    id: int
    customer: Customer
    car: Car
    start_date: str
    planned_end_date: str
    actaul_end_date: str
    created_at: str

    def __init__(
        self,
        id: int,
        customer: Customer,
        car: Car,
        start_date: str,
        planned_end_date: str,
        actaul_end_date: str,
        created_at: str,
    ) -> None:
        self.id = id
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.planned_end_date = planned_end_date
        self.actaul_end_date = actaul_end_date
        self.created_at = created_at
