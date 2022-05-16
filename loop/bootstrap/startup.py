from fastapi import FastAPI, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from loop.config import config

from loop.routes import users

class Loop(FastAPI):
    async def configure(self):
        self.include_router(users.router)


app = Loop(
    title="Loop", 
    description="Moving through"
    )

@app.on_event("startup")
async def startup():
    await app.configure()

register_tortoise(
        app,
        config={
            "connections": {"default": config.config.WRITER_DB_URL},
            "apps": {
                "models": {
                    "models": ["loop.app.models.user"],
                    "default_connection": "default",
                }
            },
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )