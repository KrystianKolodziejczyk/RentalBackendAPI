from app.modules.customers.application.services.customer_service_v3 import (
    CustomerServiceV3,
)
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.infrastrucutre.repositories.customer_repository_v3 import (
    CustomerRepositoryV3,
)
from app.modules.inventory.application.services.inventory_service_v3 import (
    InventoryServiceV3,
)
from app.modules.inventory.domain.repositories.i_inventory_repository_v2 import (
    IInventoryRepositoryV3,
)
from app.modules.inventory.domain.services.i_inventory_service_v2 import (
    IInventoryServiceV2,
)
from app.modules.inventory.infrastructure.repositories.inventory_repository_v3 import (
    InventoryRepositoryV3,
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


_inventory_repository: IInventoryRepositoryV3 = InventoryRepositoryV3(
    db_client=_db_client
)
_inventory_service: IInventoryServiceV2 = InventoryServiceV3(
    inventory_repository=_inventory_repository
)

# ====== Customers =======


_customer_repository: ICustomerRepository = CustomerRepositoryV3(db_client=_db_client)

_customer_service: ICustomerService = CustomerServiceV3(
    customer_repository=_customer_repository
)


# ======= Getters ========


def get_inventory_service() -> InventoryServiceV3:
    return _inventory_service


def get_customer_service() -> CustomerServiceV3:
    return _customer_service
