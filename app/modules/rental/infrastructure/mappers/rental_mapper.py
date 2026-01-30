from app.modules.rental.domain.models.rental import Rental


class RentalMapper:
    @staticmethod
    def rental_to_dict(rental: Rental) -> dict:
        return {
            "id": rental.id,
            "customer_id": rental.customer_id,
            "car_id": rental.car_id,
            "start_date": rental.start_date,
            "planned_end_date": rental.planned_end_date,
            "actual_end_date": rental.actual_end_date,
            "created_at": rental.created_at,
        }

    @staticmethod
    def dict_to_rental(rental_dict: dict) -> Rental:
        return Rental(
            id=rental_dict["id"],
            customer_id=rental_dict["customer_id"],
            car_id=rental_dict["car_id"],
            start_date=rental_dict["start_date"],
            planned_end_date=rental_dict["planned_end_date"],
            actual_end_date=rental_dict["actual_end_date"],
            created_at=rental_dict["created_at"],
        )
