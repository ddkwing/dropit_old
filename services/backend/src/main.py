from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import users, notes

app = FastAPI()


origins = [
    "http://localhost:8080"
    ]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])
app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"