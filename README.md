# bff-api
Backend-for-Frontend (BFF) API

# FastAPI Example

This is a simple FastAPI application that demonstrates input and output parameters.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoint

### POST /process

Process two input parameters and return two output parameters.

**Request Body:**
```json
{
    "param1": "example",
    "param2": 42
}
```

**Response:**
```json
{
    "result1": "Processed example",
    "result2": 84
}
```

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`
