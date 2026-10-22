from fastapi import APIRouter, HTTPException

from app.schemas.requests import IPValidationRequest
from app.services.validator_service import validate_ip


router = APIRouter()


@router.post("/api/v1/validate")
def validate_ip_address(request: IPValidationRequest):

    # Call Role 1's IP validation function
    result = validate_ip(request.ip)

    # Handle invalid IP addresses
    if result["status"] == "error":
        raise HTTPException(
            status_code=400,
            detail=result["message"]
        )

    # Return data to the frontend
    return result["data"]