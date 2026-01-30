from app.modules.rental.domain.models.rental import Rental
from app.modules.rental.domain.repositories.i_rental_repository import IRentalRepository
from app.modules.rental.infrastructure.mappers.rental_mapper import RentalMapper
from app.shared.domain.services.i_sqlite_client.i_sqlite_client import ISqliteClient


class RentalRepository(IRentalRepository):
    _db_client: ISqliteClient

    def __init__(self, db_client: ISqliteClient):
        self._db_client = db_client

    async def get_rental_by_id(self, rental_id: int) -> Rental:
        query: str = """
        SELECT * FROM rentals
        WHERE id = ?
        """

        rental_dict: dict = await self._db_client.fetch_one(
            query=query, params=(rental_id,)
        )

        return RentalMapper.dict_to_rental(rental_dict=rental_dict)

    async def get_all_rentals(self) -> list[Rental]:
        query: str = """
        SELECT * FROM rentals
        """

        list_rental_dict: list[dict] = await self._db_client.fetch_all(query=query)

        return [
            RentalMapper.dict_to_rental(one_rental) for one_rental in list_rental_dict
        ]

    async def rent_car(self, rental: Rental) -> int:
        rental_dict: dict = RentalMapper.rental_to_dict(rental=rental)
        query: str = """
        INSERT INTO (customer_id, car_id, start_date, planned_end_date)
        VALUES (?, ?, ?, ?)
        """

        new_id: int = await self._db_client.execute(
            query=query,
            params=(
                rental_dict["customer_id"],
                rental_dict["car_id"],
                rental_dict["start_date"],
                rental_dict["planned_end_date"],
            ),
        )

        return new_id

    async def return_car(self, rental: Rental) -> int:
        rental_dict: dict = RentalMapper.rental_to_dict(rental=rental)
        query: str = """
        UPDATE rentals
        SET actual_end_date = ?
        WHERE customer_id = ? AND car_id = ?
        """

        await self._db_client.execute(
            query=query,
            params=(
                rental_dict["actual_end_date"],
                rental_dict["customer_id"],
                rental_dict["car_id"],
            ),
        )

        return rental_dict["car_id"]
