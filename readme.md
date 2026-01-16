# Rental Inventory API

REST API for managing a car rental system with customer management. Built with FastAPI using a layered architecture.

## Features

### Car Management
- Full CRUD operations (create, read, update, delete)
- Rental status tracking (available/rented)
- Rent and return vehicles
- Available cars counter

### Customer Management
- Full CRUD operations for customers
- Block and unlock customer accounts
- Phone number and driver license uniqueness validation
- Persistent data storage in JSON files

## Requirements

- Python 3.8+

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd rental_inventory_api
   ```

2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development mode (with auto-reload):

```bash
fastapi dev app/main.py
```

or using Uvicorn:

```bash
uvicorn app.main:app --reload
```

### Production mode:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The application will be available at: `http://127.0.0.1:8000`

## API Documentation

Interactive documentation is available after starting the application:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Cars - CRUD

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/cars/all` | Get all cars |
| `GET` | `/api/cars/all/count` | Get total number of cars |
| `GET` | `/api/cars/all/{car_id}` | Get car by ID |
| `POST` | `/api/cars/all` | Add a new car |
| `PUT` | `/api/cars/all/{car_id}` | Update a car |
| `DELETE` | `/api/cars/all/{car_id}` | Delete a car |

### Cars - Rentals

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/cars/rented` | Get available cars |
| `GET` | `/api/cars/rented/check/{car_id}` | Check availability status |
| `PATCH` | `/api/cars/rented/rent/{car_id}` | Rent a car |
| `PATCH` | `/api/cars/rented/return/{car_id}` | Return a car |

### Customers

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/customers` | Get all customers |
| `GET` | `/api/customers/{customer_id}` | Get customer by ID |
| `POST` | `/api/customers` | Create a new customer |
| `PUT` | `/api/customers/{customer_id}` | Update a customer |
| `DELETE` | `/api/customers/{customer_id}` | Delete a customer |
| `PATCH` | `/api/customers/block/{customer_id}` | Block customer account |
| `PATCH` | `/api/customers/unlock/{customer_id}` | Unlock customer account |

## Data Models

### Car

```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2022
}
```

### Customer

```json
{
  "id": 1,
  "name": "John",
  "last_name": "Doe",
  "phone_number": 123456789,
  "driver_license_id": "ABC1234567890123",
  "status": "UNLOCKED"
}
```

### Data Validation

- **name/last_name**: minimum 1 character
- **phone_number**: minimum 9 digits
- **driver_license_id**: exactly 16 characters

## Business Rules

- Cannot delete a rented car (HTTP 409)
- Cannot update a rented car (HTTP 409)
- Cannot rent an already rented car (HTTP 409)
- Cannot return an available car (HTTP 409)
- Customer phone number must be unique
- Driver license number must be unique
- New customers have default status `UNLOCKED`

## Project Architecture

The project uses a layered architecture (Clean Architecture):

```
app/
├── main.py                    # Application entry point
├── core/
│   ├── bootstrap.py           # FastAPI and router initialization
│   └── container.py           # Dependency Injection
├── modules/
│   ├── rental/                # Car rental module
│   │   ├── domain/            # Models, enums, interfaces
│   │   ├── infrastructure/    # Repository implementations
│   │   ├── application/       # Business services
│   │   └── presentation/      # Controllers, DTOs, responses
│   └── customers/             # Customer management module
│       ├── domain/
│       ├── infrastructure/
│       ├── application/
│       └── presentation/
├── shared/                    # Shared components
│   └── infrastructure/
│       └── services/
│           ├── storage_ensure/    # Database file creation
│           └── fake_database/     # JSON serialization
└── database/                  # JSON data files (auto-generated)
    └── customers.json
```

### Layers

| Layer | Responsibility |
|-------|----------------|
| **Domain** | Business models, enums, interfaces (contracts) |
| **Infrastructure** | Repository implementations, data persistence |
| **Application** | Business logic, services |
| **Presentation** | API controllers, DTOs, response schemas |

### Design Patterns

- **Repository Pattern** - data access abstraction
- **Dependency Injection** - loose coupling between components
- **Service Layer** - business logic encapsulation
- **DTO (Data Transfer Objects)** - input data validation

## Data Storage

| Module | Storage Type | Notes |
|--------|--------------|-------|
| Rental (cars) | In-memory | Data lost on restart |
| Customers | JSON file | Persistent in `database/customers.json` |

## Technologies

- **FastAPI** - web framework
- **Pydantic** - data validation
- **Uvicorn** - ASGI server
- **Python 3.8+** - programming language

## License

MIT
