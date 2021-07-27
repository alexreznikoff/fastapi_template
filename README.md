## Usage
### Install
```bash
pip install cookiecutter
```

### Run
```bash
> cookiecutter https://github.com/alexreznikoff/fastapi_template.git

project_name [new-service]: the-best-microservice
project_slug [the_best_microservice]: 
project_description [Заполните описание сервиса The best microservice]: Some description
use_postgresql [n]: y

> cd the-best-microservice

> ls -la
drwxr-xr-x  10 alex  staff   320 Jul 27 08:33 .
drwxr-xr-x  14 alex  staff   448 Jul 27 08:33 ..
-rw-r--r--   1 alex  staff  1816 Jul 27 08:33 .gitignore
-rw-r--r--@  1 alex  staff   226 Jul 27 08:33 Dockerfile
-rw-r--r--   1 alex  staff    61 Jul 27 08:33 README.md
-rw-r--r--   1 alex  staff  1977 Jul 27 08:33 alembic.ini
-rw-r--r--   1 alex  staff   330 Jul 27 08:33 main.py
-rw-r--r--   1 alex  staff   171 Jul 27 08:33 requirements.txt
drwxr-xr-x   4 alex  staff   128 Jul 27 08:33 tests
drwxr-xr-x   7 alex  staff   224 Jul 27 08:33 the_best_microservice

```

