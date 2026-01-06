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

To start the server, run:
```
uvicorn app.main:app --reload
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

## Note on Current State

The whole program is not finished. The main file (`app/main.py`) is essentially the same as the controllers, and everything has been imported into the presentation layer's controllers. The architecture needs proper separation between layers, with dependency injection and proper initialization handled in the main application file rather than within the controller.

## Technologies Used

- FastAPI
- Python
- Uvicorn (for serving the app)