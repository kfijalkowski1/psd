import json
import os

from kafka import KafkaConsumer


def main() -> None:
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    output_topic = os.getenv("KAFKA_OUTPUT_TOPIC", "temperature-below-zero")

    consumer = KafkaConsumer(
        output_topic,
        bootstrap_servers=[bootstrap_servers],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="below-zero-demo-consumer",
        value_deserializer=lambda payload: json.loads(payload.decode("utf-8")),
    )

    print(
        f"Consumer started. Reading from '{output_topic}' via {bootstrap_servers}."
    )
    for message in consumer:
        print(f"received <- {message.value}")


if __name__ == "__main__":
    main()
