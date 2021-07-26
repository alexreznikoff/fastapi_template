from fastapi import APIRouter, FastAPI
from
from starlette.middleware import Middleware

from {{ cookiecutter.project_slug }}.app.logging import configure_logging
from {{ cookiecutter.project_slug }}.app.middleware import RequestIdMiddleware
from {{ cookiecutter.project_slug }}.api.views.demo import demo_router
{% if cookiecutter.use_postgresql | lower == "y" %}
from {{ cookiecutter.project_slug }}.database.db import db
{% endif %}

status_router = APIRouter(tags=["health_check"])

{% if cookiecutter.use_postgresql | lower == "y" %}
async def db_connect():
    await db.connect()


async def db_disconnect():
    await db.disconnect()
{% endif %}


@status_router.get("/status")
def health_check():
    return {"status": "ok"}


def create_app():
    configure_logging()
    app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        {% if cookiecutter.use_postgresql | lower == "y" %}
        on_startup=[db_connect],
        on_shutdown=[db_disconnect],
        {% endif %}
        middleware=[Middleware(RequestIdMiddleware),],
    )
    app.include_router(status_router)
    app.include_router(demo_router)
    return app

