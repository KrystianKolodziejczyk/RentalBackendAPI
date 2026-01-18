from app.modules.customers.application.services.customer_service import CustomerService
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.infrastrucutre.repositories.customer_repository_v2 import (
    CustomerRepositoryV2,
)
from app.modules.rental.domain.repositories.i_rental_repository_v2 import (
    IRentalRepositoryV2,
)
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.infrastructure.repositories.rental_repository_v2 import (
    RentalRepositoryV2,
)
from app.modules.rental.application.services.rental_service_v2 import RentalServiceV2
from app.shared.infrastructure.services.storage_ensure.storage_ensure import (
    StorageEnsure,
)


_rental_repository: IRentalRepositoryV2 = RentalRepositoryV2()
_rental_service: IRentalService = RentalServiceV2(rental_repository=_rental_repository)
_customer_repository: ICustomerRepository = CustomerRepositoryV2(
    path=StorageEnsure.get_path(fileName="customers.json")
)
_customer_service: ICustomerService = CustomerService(
    customerRepository=_customer_repository
)


def get_rental_service() -> RentalServiceV2:
    return _rental_service


def get_customer_service() -> CustomerService:
    return _customer_service
