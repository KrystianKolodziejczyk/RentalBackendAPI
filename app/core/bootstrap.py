from fastapi import FastAPI
from app.modules.inventory.presentation.controllers.inventory_controller import (
    router as inventory_router,
)

from app.modules.customers.presentation.controllers.cutomer_controller import (
    router as customer_router,
)


def create_app():
    app = FastAPI()
    app.include_router(router=customer_router, prefix="/api")
    app.include_router(router=inventory_router, prefix="/api")
    return app
