from fastapi import FastAPI

my_api = FastAPI()

users = [
    {"id": 1, "name": "Vlad", "age": 30},
    {"id": 2, "name": "Kostya", "age": 30},
    {"id": 3, "name": "Lasha", "age": 30}
]


@my_api.get("/")
async def root():
    return {"message": "Test FastAPI"}


@my_api.get("/users")
def read_users():
    return users


@my_api.get("/users/{user_id}")
def read_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}


@my_api.post("/users")
def create_user(user: dict):
    user_id = max(user["id"] for user in users) + 1
    user["id"] = user_id
    users.append(user)
    return user


@my_api.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            users[i] = {**u, **user}
            return users[i]
    return {"error": "User not found"}


@my_api.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}
