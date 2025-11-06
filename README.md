# Resume Backend

A minimal FastAPI application that returns "Hello from backend" at the root endpoint.

## Requirements

- Python 3.11+
- pip

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

Run the server using uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Using Docker

1. Build the Docker image:
```bash
docker build -t resume-backend .
```

2. Run the container:
```bash
docker run -p 8000:8000 resume-backend
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Returns "Hello from backend"

## Testing

Visit `http://localhost:8000` in your browser or use curl:
```bash
curl http://localhost:8000
```

