import json
import os
import random
import time
from datetime import datetime, timezone

from kafka import KafkaProducer


def serializer(payload: dict) -> bytes:
    return json.dumps(payload).encode("utf-8")


def generate_temperature_event() -> dict:
    return {
        "sensor_id": f"sensor-{random.randint(1, 8):02d}",
        "temperature_c": round(random.uniform(-20.0, 35.0), 2),
        "event_ts": datetime.now(timezone.utc).isoformat(),
    }


def main() -> None:
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    input_topic = os.getenv("KAFKA_INPUT_TOPIC", "temperature-input")
    interval_seconds = float(os.getenv("PRODUCER_INTERVAL_SECONDS", "1.0"))

    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_servers],
        value_serializer=serializer,
    )

    print(
        f"Producer started. Sending events to '{input_topic}' via {bootstrap_servers}."
    )
    while True:
        event = generate_temperature_event()
        producer.send(input_topic, event)
        producer.flush()
        print(f"sent -> {event}")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    main()
