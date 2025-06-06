# Placeholder for mqtt_rest_bridge.py

import os
import json
import paho.mqtt.client as mqtt
import requests
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv('MQTT_BROKER', 'maps')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'http://webhook-mock:9999/webhook')

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("weather.responses")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"Received message on {msg.topic}: {payload}")
        
        # Forward to webhook
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"Webhook response: {response.status_code}")
    except Exception as e:
        print(f"Error processing message: {e}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Connecting to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    main()
