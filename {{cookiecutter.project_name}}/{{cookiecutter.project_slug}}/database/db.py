from databases import Database

from {{ cookiecutter.project_slug }}.app.config import environment, settings

db = Database(settings.PG_DSN, min_size=2, max_size=10)
