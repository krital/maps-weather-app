FROM python:3.11-slim

WORKDIR /app

COPY maps_weather_worker.py ./

RUN pip install requests watchdog

CMD ["watchmedo", "auto-restart", "--pattern=*.py", "--recursive", "--", "python", "maps_weather_worker.py"]