from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "REST API is running"}


@app.get("/users")
def get_users():
    return {
        "users": [
            {
                "id": 1,
                "name": "Ali",
                "email": "ali@example.com"
            },
            {
                "id": 2,
                "name": "Ahmed",
                "email": "ahmed@example.com"
            }
        ]
    }