from app.modules.customers.domain.models.customer import Customer
from app.modules.customers.domain.services.i_customer_service import ICustomerService
from app.modules.inventory.domain.enums.rent_status_enum import RentStatusEnum
from app.modules.inventory.domain.models.car import Car
from app.modules.inventory.domain.services.i_inventory_service import IInventoryService
from app.modules.rental.domain.models.rental import Rental
from app.modules.rental.domain.rental_exceptions.rental_exceptions import (
    ActiveRentalsNotFoundException,
    RentalNotFoundException,
)
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.domain.services.i_rental_service import IRentalService
from app.modules.rental.presentation.dto.rent_car_dto import RentCarDto


class RentalService(IRentalService):
    _rental_repository: IRentalRepository
    _customer_service: ICustomerService
    _inventory_service: IInventoryService

    def __init__(
        self,
        rental_repository: IRentalRepository,
        customer_service: ICustomerService,
        inventory_service: IInventoryService,
    ) -> None:
        self._rental_repository: IRentalRepository = rental_repository
        self._customer_service: ICustomerService = customer_service
        self._inventory_service: IInventoryService = inventory_service

    async def get_rental_by_id(self, rental_id: int) -> Rental | None:
        rental: Rental = await self._rental_repository.get_rental_by_id(
            rental_id=rental_id
        )

        if rental is None:
            raise RentalNotFoundException(rental_id=rental_id)

        return rental

    async def get_all_rentals(self) -> list[Rental]:
        return await self._rental_repository.get_all_rentals()

    # Returns rented car id
    async def rent_car(self, rent_car_dto: RentCarDto) -> int:
        car: Car = await self._inventory_service.get_car_by_id(
            car_id=rent_car_dto.car_id
        )
        customer: Customer = await self._customer_service.get_customer_by_id(
            customer_id=rent_car_dto.customer_id
        )

        car.ensure_available(action="rent")
        customer.ensure_not_blocked()

        rental = Rental.create(
            customer_id=rent_car_dto.customer_id,
            car_id=rent_car_dto.car_id,
            start_date=rent_car_dto.start_date,
            planned_end_date=rent_car_dto.planned_end_date,
        )

        car.change_status(new_status=RentStatusEnum.RENTED)
        await self._inventory_service.change_car_status(car=car)

        return await self._rental_repository.rent_car(rental=rental)

    # Returns returned car id
    async def return_car(self, rental_id: int) -> int:
        rental: Rental = await self._rental_repository.get_rental_by_id(
            rental_id=rental_id
        )
        car: Car = await self._inventory_service.get_car_by_id(car_id=rental.car_id)
        car.ensure_rented(action="return")
        rental.complete_return()

        car_id: int = await self._rental_repository.return_car(rental=rental)

        car.change_status(new_status=RentStatusEnum.AVAILABLE)
        await self._inventory_service.change_car_status(car=car)

        return car_id

    # Returns only active rentals
    async def get_active_rentals(self) -> list[Rental] | None:
        rentals: list[Rental] = await self._rental_repository.get_active_rentals()

        if not rentals:
            raise ActiveRentalsNotFoundException

        return rentals
