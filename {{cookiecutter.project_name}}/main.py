import uvicorn

from {{ cookiecutter.project_slug}}.app.config import settings
from {{ cookiecutter.project_slug}}.app.fastapi import create_app


if __name__ == "__main__":
    uvicorn.run(
        "main:create_app",
        host=settings.HOST,
        port=settings.PORT,
        log_level=settings.LOG_LEVEL.lower(),
        reload=False,
    )
