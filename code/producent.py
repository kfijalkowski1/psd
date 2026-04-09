import time
import json
import requests
from datetime import datetime
from kafka import KafkaProducer

# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode("utf-8")

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=serializer
)

def get_singapore_temperature():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=1.3521&longitude=103.8198"
        "&current=temperature_2m"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    return {
        "city": "Singapore",
        "temperature_c": data["current"]["temperature_2m"],
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    while True:
        try:
            message = get_singapore_temperature()

            print(f'Producing message @ {datetime.now()} | Message = {message}')
            producer.send("messages", message)

        except Exception as e:
            print(f"Error fetching or sending temperature: {e}")

        time.sleep(1)
