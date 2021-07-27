import re
import sys


PROJECT_RE_SLUG = re.compile(r"^[_a-zA-Z0-9]+")
PROJECT_NAME_RE = re.compile(r"^[_a-zA-Z0-9-]+")

project_name = "{{ cookiecutter.project_name }}"
project_slug = "{{ cookiecutter.project_slug }}"
use_postgresql = "{{ cookiecutter.use_postgresql }}".lower()


if __name__ == "__main__":
    exit_code = 0

    if not PROJECT_RE_SLUG.fullmatch(project_slug):
        print(f"ERROR: The project slug {project_slug} is not a valid Python module name.")
        exit_code = 1

    if not PROJECT_NAME_RE.fullmatch(project_name):
        print(f"ERROR: {project_name=} contains bad symbols")
        exit_code = 1

    sys.exit(exit_code)




