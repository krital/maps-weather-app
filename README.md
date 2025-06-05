# MAPS Messaging AI Weather App

This project demonstrates how to connect an AI assistant (e.g. GPT with function calling) to the [MAPS Messaging](https://mapsmessaging.io) event bus to query real-time weather data. It uses OpenWeatherMap, topic-based message orchestration, and a local webhook for simulating AI interaction.

## 📦 Services Included

- **MAPS Messaging** – Core broker (REST, MQTT, NATS)
- **Weather Worker** – Subscribes to MAPS and calls OpenWeather
- **MQTT-to-REST Bridge** – Forwards weather responses to webhook
- **Webhook Mock** – Local Flask app to simulate AI input/output

## 🚀 Quick Start

```bash
docker compose up --build
```

📍 Access MAPS UI at: `http://localhost:8080`  
📍 Webhook logs available at: `http://localhost:5001`

## 🧪 Simulate AI Weather Request

```bash
curl -X POST http://localhost:8080/v1/messages/publish \
  -H "Authorization: Bearer supersecrettoken" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "weather.requests",
    "message": {
      "location": { "city": "London" },
      "preferences": { "unit": "metric" }
    }
  }'
```

## 🧠 GPT Function Schema

See `gpt-function-schema.json` for agent integration.

## 🛠 Developer Mode

Auto-restarts the weather worker on code changes:

```bash
docker compose -f docker-compose.yaml -f docker-compose.override.yaml up --build
```

## 🔒 Secrets

Update these values in your environment or `.env`:

- `MAPS_TOKEN=supersecrettoken`
- `OPENWEATHERMAP_API_KEY=your_key`

---

## ✅ GitHub Actions CI

Builds all Docker images to validate syntax and structure.