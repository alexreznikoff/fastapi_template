FROM python:3.9.2-slim

RUN mkdir -p /var/log/huntflow/

EXPOSE 9900

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --default-timeout=100 -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["python3", "main.py"]