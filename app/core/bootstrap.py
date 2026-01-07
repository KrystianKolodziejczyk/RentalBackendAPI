from fastapi import FastAPI
from app.modules.rental.presentation.controllers.rental_controller import (
    router as rental_router,
)


def create_app():
    app = FastAPI()
    app.include_router(router=rental_router, prefix="/api")
    return app
