
import requests
import json
from datetime import datetime

# Simulated message received from MAPS Messaging
incoming_message = {
    "location": { "city": "London" },
    "preferences": { "unit": "metric" }
}

def fetch_weather(city, unit):
    api_key = "<your-openweathermap-api-key>"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
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

# Replace this URL with your actual MAPS instance endpoint
maps_url = "https://your.maps.instance/v1/messages/publish"
headers = {
    "Authorization": "Bearer <your-token>",
    "Content-Type": "application/json"
}

response = requests.post(maps_url, headers=headers, data=json.dumps(publish_payload))
print(response.status_code, response.text)
