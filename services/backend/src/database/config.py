import os


TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:postgres@localhost:5432/dropit"},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
