import os
import requests
import json
from datetime import datetime

# Simulated message received from MAPS Messaging
incoming_message = {
    "location": { "city": "London" },
    "preferences": { "unit": "metric" }
}

def fetch_weather(city, unit):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENWEATHERMAP_API_KEY not found in environment")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print("⚠️ Raw OpenWeather response:", json.dumps(data, indent=2))

    if "main" not in data:
        raise ValueError(f"OpenWeather response error: {data}")

    return {
        "location": {"city": city},
        "temperature": data["main"]["temp"],
        "conditions": data["weather"][0]["main"],
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

weather_data = fetch_weather(incoming_message["location"]["city"],
                              incoming_message["preferences"]["unit"])

publish_payload = {
    "topic": "weather.responses",
    "message": weather_data
}

maps_host = os.getenv("MAPS_URL", "http://localhost:8080")
maps_url = f"{maps_host}/v1/messages/publish"
headers = {
    "Authorization": f"Bearer {os.getenv('MAPS_TOKEN', 'supersecrettoken')}",
    "Content-Type": "application/json"
}

try:
    response = requests.post(maps_url, headers=headers, data=json.dumps(publish_payload))
    print("📬 Published to MAPS:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("❌ Failed to publish to MAPS:", str(e))