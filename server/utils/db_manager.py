from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from server.utils.constants import DATABASE_URI, DB_PATH

MIGRATION_CONFIG = {
    "connections": {"default": DATABASE_URI},
    "apps": {
        "models": {
            "models": ["server.models.database", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URI,
        modules={"models": [DB_PATH]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
