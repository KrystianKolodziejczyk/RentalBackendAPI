from app.modules.customers.application.services.customer_service import (
    CustomerService,
)
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.infrastructure.repositories.customer_repository import (
    CustomerRepository,
)
from app.modules.inventory.application.services.inventory_service import (
    InventoryService,
)
from app.modules.inventory.domain.repositories.i_inventory_repository import (
    IInventoryRepository,
)
from app.modules.inventory.domain.services.i_inventory_service import (
    IInventoryService,
)
from app.modules.inventory.infrastructure.repositories.inventory_repository import (
    InventoryRepository,
)
from app.modules.rental.application.services.rental_service import RentalService
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.infrastructure.repositories.rental_repository import (
    RentalRepository,
)
from app.shared.domain.services.i_sqlite_client.i_sqlite_client import ISqliteClient
from app.shared.infrastructure.services.sqlite_client.sqlite_client import SqliteClient
from app.shared.infrastructure.services.storage_ensure.storage_ensure import (
    StorageEnsure,
)

_db_client: ISqliteClient = SqliteClient(
    path=StorageEnsure.get_path("rental_database.db")
)

# ====== Inventory =======


_inventory_repository: IInventoryRepository = InventoryRepository(db_client=_db_client)
_inventory_service: IInventoryService = InventoryService(
    inventory_repository=_inventory_repository
)

# ====== Customers =======


_customer_repository: ICustomerRepository = CustomerRepository(db_client=_db_client)

_customer_service: ICustomerService = CustomerService(
    customer_repository=_customer_repository
)

# ======= Rental =========

_rental_repository: IRentalRepository = RentalRepository(db_client=_db_client)

_rental_service: IRentalService = RentalService(
    rental_repository=_rental_repository,
    customer_service=_customer_service,
    inventory_service=_inventory_service,
)


# ======= Getters ========


def get_inventory_service() -> InventoryService:
    return _inventory_service


def get_customer_service() -> CustomerService:
    return _customer_service


def get_rental_service() -> RentalService:
    return _rental_service
