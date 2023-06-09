import os

from fastapi import FastAPI

from app.models.database import database
from app.routers import users

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router)

if __name__ == "__main__":
    os.system("make server")
