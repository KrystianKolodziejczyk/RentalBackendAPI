from app.modules.customers.application.services.customer_service_v2 import (
    CustomerServiceV2,
)
from app.modules.customers.domain.repositories.i_customer_repository import (
    ICustomerRepository,
)
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.customers.infrastrucutre.repositories.customer_repository_v2 import (
    CustomerRepositoryV2,
)
from app.modules.inventory.domain.repositories.i_inventory_repository_v2 import (
    IInventoryRepositoryV2,
)
from app.modules.inventory.domain.services.i_inventory_service import IInventoryService
from app.modules.inventory.infrastructure.repositories.inventory_repository_v2 import (
    InventoryRepositoryV2,
)
from app.modules.inventory.application.services.inventory_service_v2 import InventoryServiceV2
from app.shared.infrastructure.services.storage_ensure.storage_ensure import (
    StorageEnsure,
)


_inventory_repository: IInventoryRepositoryV2 = InventoryRepositoryV2(
    path=StorageEnsure.get_path("store_items.json")
)
_inventory_service: IInventoryService = InventoryServiceV2(inventory_repository=_inventory_repository)
_customer_repository: ICustomerRepository = CustomerRepositoryV2(
    path=StorageEnsure.get_path("customers.json")
)
_customer_service: ICustomerService = CustomerServiceV2(
    customer_repository=_customer_repository
)


def get_inventory_service() -> InventoryServiceV2:
    return _inventory_service


def get_customer_service() -> CustomerServiceV2:
    return _customer_service
