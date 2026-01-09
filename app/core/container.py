from app.modules.customers.application.customer_service import CustomerService
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.infrastrucutre.repositories.customer_repository import (
    CustomerRepository,
)
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.infrastructure.repositories.rental_repository import (
    RentalRepository,
)
from app.modules.rental.application.services.rental_service import RentalService


_rental_repository: IRentalRepository = RentalRepository()
_rental_service: IRentalService = RentalService(rental_repository=_rental_repository)
_customer_repository: ICustomerRepository = CustomerRepository()
_customer_service: ICustomerService = CustomerService(
    customerRepository=_customer_repository
)


def get_rental_service() -> RentalService:
    return _rental_service


def get_customer_service() -> CustomerService:
    return _customer_service
