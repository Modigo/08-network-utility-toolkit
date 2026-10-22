from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app


client = TestClient(app)


# Test 1: API homepage
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


# Test 2: Health check
def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# Test 3: Valid IP address
def test_valid_ip():
    response = client.post(
        "/api/v1/validate",
        json={"ip": "192.168.1.1"}
    )

    assert response.status_code == 200
    assert response.json()["ip"] == "192.168.1.1"


# Test 4: Invalid IP address
def test_invalid_ip():
    response = client.post(
        "/api/v1/validate",
        json={"ip": "999.999.999.999"}
    )

    assert response.status_code == 400


# Test 5: Subnet calculation
def test_subnet():
    response = client.post(
        "/api/v1/subnet",
        json={
            "ip": "192.168.1.10",
            "cidr": 24
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["network_address"] == "192.168.1.0"
    assert data["broadcast_address"] == "192.168.1.255"
    assert data["usable_hosts"] == 254


# Test 6: Invalid subnet
def test_invalid_subnet():
    response = client.post(
        "/api/v1/subnet",
        json={
            "ip": "192.168.1.10",
            "cidr": 50
        }
    )

    assert response.status_code == 400


# Test 7: DNS lookup
@patch("app.api.routes.dns.lookup_dns")
def test_dns(mock_lookup):
    mock_lookup.return_value = {
        "success": True,
        "domain": "google.com",
        "record_type": "A",
        "records": ["142.250.190.14"]
    }

    response = client.get(
        "/api/v1/dns",
        params={
            "domain": "google.com",
            "type": "A"
        }
    )

    assert response.status_code == 200
    assert response.json()["domain"] == "google.com"
    assert response.json()["type"] == "A"


# Test 8: Reverse DNS lookup
@patch("app.api.routes.dns.reverse_dns_lookup")
def test_reverse_dns(mock_reverse):
    mock_reverse.return_value = {
        "success": True,
        "ip_address": "8.8.8.8",
        "hostnames": ["dns.google"]
    }

    response = client.get(
        "/api/v1/dns",
        params={
            "domain": "8.8.8.8",
            "type": "PTR"
        }
    )

    assert response.status_code == 200
    assert response.json()["records"] == ["dns.google"]