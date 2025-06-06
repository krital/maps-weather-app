# Placeholder for maps_weather_worker.py

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

MAPS_URL = os.getenv('MAPS_URL', 'http://[::1]:8080/v1/messages/publish')
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
MAPS_TOKEN = os.getenv('MAPS_TOKEN', 'supersecrettoken')

def get_weather(city, unit='metric'):
    """Get weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': unit
    }
    response = requests.get(url, params=params)
    return response.json()

def publish_to_maps(topic, message):
    """Publish message to MAPS."""
    headers = {
        'Authorization': f'Bearer {MAPS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'topic': topic,
        'message': message
    }
    response = requests.post(MAPS_URL, headers=headers, json=data)
    return response.json()

def main():
    print("Weather worker started...")
    while True:
        try:
            # Subscribe to weather requests
            response = requests.get(
                f"{MAPS_URL}/subscribe",
                headers={'Authorization': f'Bearer {MAPS_TOKEN}'},
                params={'topic': 'weather.requests'}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('message'):
                    location = data['message'].get('location', {}).get('city')
                    preferences = data['message'].get('preferences', {})
                    unit = preferences.get('unit', 'metric')
                    
                    if location:
                        weather_data = get_weather(location, unit)
                        publish_to_maps('weather.responses', weather_data)
                        
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == '__main__':
    main()
