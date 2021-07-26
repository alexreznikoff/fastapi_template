import os
import shutil


PROJECT_DIRECTORY = os.path.relpath(os.path.curdir)

project_slug = "{{ cookiecutter.project_slug }}"
use_postgresql = "{{ cookiecutter.use_postgresql }}".lower()


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(directory: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, directory))


if __name__ == "__main__":
    if use_postgresql != "y":
        remove_file("alembic.ini")
        remove_directory(f"{project_slug}/database")

