import paho.mqtt.client as mqtt
import requests
import json

MQTT_BROKER = "maps"
MQTT_PORT = 1883
TOPIC = "weather.responses"
WEBHOOK_URL = "http://your-agent-endpoint/webhook"  # Change as needed

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        print(f"Forwarding to webhook: {data}")
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Error forwarding message: {e}")

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(TOPIC)
client.on_message = on_message

print("MQTT to REST bridge running...")
client.loop_forever()