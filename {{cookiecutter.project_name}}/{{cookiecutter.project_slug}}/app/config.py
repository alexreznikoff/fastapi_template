import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PORT: int = 9950
    HOST: str = "127.0.0.1"

    TIMEOUT: int = 5
    LOG_LEVEL: str = "INFO"
    LOG_FILENAME: str = ""

    {% if cookiecutter.use_postgresql | lower == "y" %}
    PG_HOST: str = "127.0.0.1"
    PG_PORT: int = 5432
    PG_USER: str = "postgres"
    PG_PASS: str = "postgres"
    PG_DB_NAME: str

    @property
    def PG_DSN(self):
        dsn = "postgresql://{}:{}@{}:{}/{}"
        return dsn.format(self.PG_USER, self.PG_PASS, self.PG_HOST, self.PG_PORT, self.PG_DB_NAME)
    {% endif %}

    class Config:
        case_sensitive = False


environment: str = os.getenv("ENVIRONMENT", "docker").lower()
settings = Settings(_env_file=f"config/{environment}.env")
