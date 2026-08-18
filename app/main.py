from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str


users = [
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


@app.get("/")
def home():
    return {"message": "REST API is running"}


@app.get("/users")
def get_users():
    return {"users": users}


@app.post("/users")
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }