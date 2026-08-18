from fastapi import FastAPI, HTTPException, status
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
        "name": "Ahmad",
        "email": "ahmad@example.com"
    }
]


@app.get("/")
def home():
    return {"message": "REST API is running"}


@app.get("/users")
def get_users():
    return {"users": users}


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):

    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

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