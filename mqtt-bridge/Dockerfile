FROM python:3.11-slim

WORKDIR /bridge

COPY mqtt_rest_bridge.py ./

RUN pip install paho-mqtt requests

CMD ["python", "mqtt_rest_bridge.py"]