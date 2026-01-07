from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.infrastructure.repositories.rental_repository import (
    RentalRepository,
)
from app.modules.rental.application.services.rental_service import RentalService


_rental_repository: IRentalRepository = RentalRepository()
_rental_service: IRentalService = RentalService(rental_repository=_rental_repository)


def get_rental_service() -> RentalService:
    return _rental_service
