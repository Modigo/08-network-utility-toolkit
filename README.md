🌐 Team 11 — Network Utility Toolkit

A web-based networking utility developed by Team 11 to simplify IP address validation, subnet calculations, DNS lookups, and reverse DNS lookups.

The application provides a user-friendly interface connected to a Python FastAPI backend.

🚀 Live Application

Frontend:
https://team11-network-toolkit-frontend.onrender.com

Backend API:
https://team11-network-toolkit-api.onrender.com

Interactive API Documentation:
https://team11-network-toolkit-api.onrender.com/docs

GitHub Repository:
https://github.com/promzycgold-code/08-network-utility-toolkit

📌 Project Overview

The Network Utility Toolkit helps users perform common networking operations without manually calculating network information or using complex command-line tools.

It combines a simple frontend interface with a REST API to provide accurate networking information.

✨ Features

1. IP Address Validation

- Validates IP addresses.
- Identifies valid and invalid IP address formats.
- Provides useful information about valid addresses.

2. Subnet Calculator

- Calculates subnet information using IP addresses and CIDR prefixes.
- Determines network addresses and subnet masks.
- Provides information about available host addresses.

3. DNS Lookup

- Retrieves DNS records for domain names.
- Supports A, AAAA, MX, TXT, and NS records.
- Displays DNS lookup results.

4. Reverse DNS Lookup

- Uses PTR records to perform reverse DNS lookups.
- Attempts to identify hostnames associated with IP addresses.
- Available through the backend DNS API using the PTR record type.

🛠️ Technologies Used

Frontend

- HTML5
- CSS3
- JavaScript

Backend

- Python
- FastAPI
- Uvicorn
- dnspython
- Pydantic

Testing

- pytest
- httpx
- Node.js test runner

Deployment

- Render — backend API
- Render — frontend static website
- GitHub — version control and collaboration

📁 Project Structure

08-network-utility-toolkit/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── validator.py
│   │   │       ├── subnet.py
│   │   │       └── dns.py
│   │   │
│   │   ├── services/
│   │   │   ├── validator_service.py
│   │   │   ├── subnet_service.py
│   │   │   ├── dns_service.py
│   │   │   └── reverse_dns_service.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   ├── api.js
│   ├── config.js
│   ├── validators.js
│   ├── mock.js
│   └── package.json
│
└── README.md

⚙️ Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/promzycgold-code/08-network-utility-toolkit.git

Navigate into the project:

cd 08-network-utility-toolkit

Step 2: Set Up the Backend

Navigate into the backend directory:

cd backend

Create a virtual environment:

python -m venv venv

Activate the virtual environment.

On Windows:

venv\Scripts\activate

On Linux or macOS:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Start the backend server:

uvicorn app.main:app --reload

The backend will run at:

http://localhost:8000

API documentation will be available at:

http://localhost:8000/docs

Step 3: Set Up the Frontend

Open another terminal and navigate into the frontend directory:

cd frontend

Start a local server:

python3 -m http.server 5500

Open the application in your browser:

http://localhost:5500

For local development, update "frontend/config.js" to:

export const API_BASE = "http://localhost:8000";
export const USE_MOCK = false;

For the deployed application, use the production backend URL instead.

🔌 API Endpoints

Method| Endpoint| Description
GET| "/"| API welcome message
GET| "/health"| Backend health check
POST| "/api/v1/validate"| Validate an IP address
POST| "/api/v1/subnet"| Calculate subnet information
GET| "/api/v1/dns"| Perform DNS lookup
GET| "/api/v1/dns?domain=8.8.8.8&type=PTR"| Perform reverse DNS lookup

Example: IP Validation

Endpoint

POST /api/v1/validate

Request

{
  "ip": "192.168.1.1"
}

Example: Subnet Calculation

Endpoint

POST /api/v1/subnet

Request

{
  "ip": "192.168.1.10",
  "cidr": 24
}

Example: DNS Lookup

GET /api/v1/dns?domain=google.com&type=A

Example: Reverse DNS Lookup

GET /api/v1/dns?domain=8.8.8.8&type=PTR

🧪 Testing

Backend tests are located in:

backend/tests/

To run the backend tests:

cd backend
python -m pytest

To run the frontend tests:

cd frontend
npm test

The tests help verify networking calculations, validation logic, and DNS functionality.

☁️ Deployment

The project uses Render for deployment.

Backend Deployment

The FastAPI backend is deployed as a Render Web Service.

The application runs using Uvicorn and exposes REST API endpoints.

Frontend Deployment

The frontend is deployed as a Render Static Site.

It communicates with the deployed backend through the API URL configured in "frontend/config.js".

Production configuration:

export const API_BASE = "https://team11-network-toolkit-api.onrender.com";
export const USE_MOCK = false;

CORS is configured in the backend to allow requests from the deployed frontend.

👥 Team Contributions

This project was developed collaboratively by four team members.

Role 1 — Calculation Library Developer

- IP address validation.
- Subnet calculation.
- Core networking calculations and tests.

Role 2 — DNS Module Developer and Project Leader

- DNS lookup implementation.
- Reverse DNS lookup implementation.
- Project coordination and integration support.

Role 3 — API and Integration Engineer

- FastAPI application development.
- API endpoint integration.
- Backend deployment.
- API testing and error handling.

Role 4 — Frontend Developer

- User interface development.
- HTML, CSS, and JavaScript implementation.
- Frontend and backend integration.
- Frontend deployment.

🔒 Error Handling and Validation

The application includes validation and error handling for common problems such as:

- Invalid IP addresses.
- Incorrect subnet prefixes.
- Invalid domain names.
- DNS lookup failures.
- Backend connection errors.

📈 Future Improvements

Potential future enhancements include:

- A dedicated reverse DNS lookup interface.
- Additional DNS record types.
- Improved mobile responsiveness.
- Expanded automated test coverage.
- Network diagnostic tools such as ping and traceroute.
- Additional deployment monitoring.

🎯 Learning Outcomes

This project provided practical experience in:

- Python programming.
- Networking fundamentals.
- IP addressing and subnetting.
- DNS resolution.
- REST API development.
- Frontend and backend integration.
- Git and GitHub collaboration.
- Cloud deployment.

📄 Conclusion

The Team 11 Network Utility Toolkit demonstrates how networking concepts can be implemented in a practical web application.

By combining Python, FastAPI, JavaScript, and cloud deployment, the team developed an accessible networking toolkit that supports common network administration tasks.

Developed by Team 11.
