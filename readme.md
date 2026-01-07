# Rental Inventory API

This is a FastAPI-based API for managing a rental inventory system, focused on cars for rental purposes.

## Features

- Retrieve all cars in the inventory
- Get the total count of cars
- Fetch a specific car by its ID
- Add a new car to the inventory
- Delete a car from the inventory
- Get a list of available (not rented) cars
- Check the availability status of a specific car
- Rent a car (change status to rented)
- Return a car (change status to available)

## Installation

1. Ensure you have Python installed (version 3.8 or higher recommended).
2. Clone this repository.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the server, run one of the following commands:

Using Uvicorn:
```
uvicorn app.main:app --reload
```

Using FastAPI CLI (recommended for development):
```
fastapi dev app/main.py
```

The API will be available at `http://127.0.0.1:8000`.

You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `GET /api/cars/all` - Get all cars
- `GET /api/cars/all/count` - Get total number of cars
- `GET /api/cars/all/{car_id}` - Get a specific car by ID
- `POST /api/cars/all` - Add a new car
- `DELETE /api/cars/all/{car_id}` - Delete a car by ID
- `GET /api/cars/rented` - Get available cars (note: endpoint name might be misleading, as it returns available cars)
- `GET /api/cars/rented/check/{car_id}` - Check the availability status of a specific car
- `PATCH /api/cars/rented/rent/{car_id}` - Rent a car (change its status to rented)
- `PATCH /api/cars/rented/return/{car_id}` - Return a car (change its status to available)

## Project Structure

The project follows a layered architecture:
- **Domain**: Contains business logic models, enums, and interfaces
- **Infrastructure**: Handles data persistence (repositories)
- **Application**: Contains services
- **Presentation**: Controllers, DTOs, and response models

```
readme.md
requirements.txt
app/
    __init__.py
    main.py
    core/
        __init__.py
        bootstrap.py
        container.py
    modules/
        rental/
            __init__.py
            application/
                services/
                    rental_service.py
            domain/
                enums/
                    rent_status_enum.py
                models/
                    car.py
                    store_item.py
                repositories/
                    i_rental_repository.py
                services/
                    i_rental_service.py
            infrastructure/
                repositories/
                    rental_repository.py
            presentation/
                controllers/
                    rental_controller.py
                dto/
                    create_car_dto.py
                response/
                    cars_qty_response.py
                    check_available_car_response.py
                    create_car_response.py
                    delete_car_response.py
                    get_car_response.py
                    rent_car_response.py
```

## Note on Current State

The project is now complete with proper layered architecture, dependency injection, and separation of concerns. The main application file handles initialization, while controllers focus on API endpoints, services contain business logic, and repositories manage data persistence.

## Technologies Used

- FastAPI
- Python
- Uvicorn (for serving the app)