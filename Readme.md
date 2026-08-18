# REST API Fundamentals

A REST API built with FastAPI as part of the Decode Labs Backend Development Internship.

## Features

- FastAPI application
- GET /users endpoint
- POST /users endpoint
- Pydantic request validation
- Duplicate email prevention
- HTTP status codes
- Error handling
- Swagger/OpenAPI documentation

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## Running the Project

### 1. Clone the repository

Terminal:
git clone https://github.com/Abdulwasaytahir/rest-api-fundamentals.git
cd rest-api-fundamentals

2. Create virtual environment
python -m venv venv

3. Activate virtual environment

Windows:
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Start the server
uvicorn app.main:app --reload

API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

Endpoints
Method	Endpoint	Description
GET	/	Check API status
GET	/users	Retrieve users
POST	/users	Create a new user


### Final testing 🧪


Start the server:
Terminal:
uvicorn app.main:app --reload

Then Swagger:

http://127.0.0.1:8000/docs

Test all three:

GET / → 200 OK ✅

GET /users → 200 OK + users JSON ✅

POST /users → 201 Created ✅

Duplicate email → 400 Bad Request ✅

Missing required field → 422 ✅