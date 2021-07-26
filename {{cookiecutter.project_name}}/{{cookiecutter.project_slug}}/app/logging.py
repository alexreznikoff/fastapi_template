import logging

from {{ cookiecutter.project_slug }}.app.config import settings
from {{ cookiecutter.project_slug }}.utils.request_id import request_id_manager


LOG_FORMAT = "[%(process)s %(asctime)s %(levelname)s %(name)s %(x_request_id)s] %(message)s"


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.x_request_id = request_id_manager.get()
        return True


def configure_logging():
    handlers = [logging.StreamHandler()]
    if settings.LOG_FILENAME:
        handlers.append(logging.FileHandler(settings.LOG_FILENAME))

    for h in handlers:
        h.addFilter(RequestIdFilter())

    {% if cookiecutter.use_postgresql | lower == "y" %}
    logging.getLogger("aiopg").setLevel(settings.LOG_LEVEL)
    logging.getLogger("databases").setLevel("WARNING")
    {% endif %}

    logging.basicConfig(level=settings.LOG_LEVEL, format=LOG_FORMAT, handlers=handlers)
