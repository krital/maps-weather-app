FROM python:3.11-slim

WORKDIR /app

COPY webhook_server.py .

RUN pip install flask

CMD ["python", "webhook_server.py"]