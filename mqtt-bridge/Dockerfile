FROM python:3.11-slim
WORKDIR /bridge
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "mqtt_rest_bridge.py"]