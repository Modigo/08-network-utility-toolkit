from fastapi import APIRouter, HTTPException, Query

from app.services.dns_service import lookup_dns
from app.services.reverse_dns_service import reverse_dns_lookup


router = APIRouter()


@router.get("/api/v1/dns")
def dns_lookup_api(
    domain: str = Query(..., min_length=1),
    type: str = Query(default="A")
):
    """
    Perform DNS lookups.

    Supported record types:
    A, AAAA, MX, TXT, NS, PTR

    PTR requests use the reverse DNS service.
    """

    record_type = type.upper()

    # Handle reverse DNS (PTR) requests
    if record_type == "PTR":

        result = reverse_dns_lookup(domain)

        if not result["success"]:
            raise HTTPException(
                status_code=400,
                detail=result["error"]
            )

        return {
            "domain": domain,
            "type": "PTR",
            "records": result["hostnames"]
        }

    # Handle regular DNS requests
    result = lookup_dns(domain, record_type)

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return {
        "domain": result["domain"],
        "type": result["record_type"],
        "records": result["records"]
    }