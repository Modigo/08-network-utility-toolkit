from pydantic import BaseModel, Field


class IPValidationRequest(BaseModel):
    ip: str


class SubnetCalculationRequest(BaseModel):
    ip: str
    cidr: int = Field(ge=0, le=128)