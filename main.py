from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "Hello from backend"


@app.get("/api/status")
def get_status():
    return {
        "status": "healthy",
        "service": "resume-backend",
        "uptime": "running"
    }


@app.get("/api/info")
def get_info():
    return {
        "name": "Resume Backend check  API",
        "version": "1.0.0",
        "description": "Backend API for Resume IQ application"
    }


@app.get("/api/stats")
def get_stats():
    return {
        "total_requests check": 42,
        "active_connections": 5,
        "response_time_ms": 12
    }


@app.get("/api/version")
def get_version():
    return {
        "api_version check": "1.0.0",
        "python_version": "3.11",
        "framework": "FastAPI"
    }

