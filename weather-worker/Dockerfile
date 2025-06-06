FROM python:3.11-slim

WORKDIR /app

COPY maps_weather_worker.py ./

RUN pip install --upgrade pip setuptools && \
    pip install requests watchdog

ENV PATH="/root/.local/bin:${PATH}"

CMD ["watchmedo", "auto-restart", "--pattern=*.py", "--recursive", "--", "python", "maps_weather_worker.py"]