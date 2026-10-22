from fastapi import APIRouter, HTTPException

from app.schemas.requests import SubnetCalculationRequest
from app.services.subnet_service import calculate_subnet


router = APIRouter()


@router.post("/api/v1/subnet")
def calculate_subnet_api(request: SubnetCalculationRequest):

    # Combine IP address and CIDR prefix
    cidr_notation = f"{request.ip}/{request.cidr}"

    # Call Role 1's subnet calculator
    result = calculate_subnet(cidr_notation)

    # Handle invalid subnet information
    if result["status"] == "error":
        raise HTTPException(
            status_code=400,
            detail=result["message"]
        )

    # Return subnet information to the frontend
    return result["data"]