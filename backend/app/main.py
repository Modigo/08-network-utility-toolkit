from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import validator, subnet, dns


# Create the FastAPI application
app = FastAPI(
    title="Team 11 Network Utility Toolkit",
    description="API for IP validation, subnet calculation, DNS lookup and reverse DNS lookup.",
    version="1.0.0"
)


# Allow the deployed frontend to communicate with the backend
origins = [
    "https://team11-network-toolkit.netlify.app",
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# Register all API routes
app.include_router(validator.router)
app.include_router(subnet.router)
app.include_router(dns.router)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Team 11 Network Utility Toolkit API",
        "status": "running",
        "version": "1.0.0"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Network Utility Toolkit API"
    }
