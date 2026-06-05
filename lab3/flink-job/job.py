import json

from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer


def main() -> None:
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    consumer = FlinkKafkaConsumer(
        topics="temperature-input",
        deserialization_schema=SimpleStringSchema(),
        properties={
            "bootstrap.servers": "kafka:29092",
            "group.id": "flink-temperature-filter",
        },
    )
    consumer.set_start_from_earliest()

    source_stream = env.add_source(consumer)

    def is_below_zero(raw_event: str) -> bool:
        try:
            payload = json.loads(raw_event)
            return float(payload.get("temperature_c", 999.0)) < 0
        except (ValueError, TypeError, json.JSONDecodeError):
            return False

    filtered_stream = source_stream.filter(is_below_zero)

    producer = FlinkKafkaProducer(
        topic="temperature-below-zero",
        serialization_schema=SimpleStringSchema(),
        producer_config={"bootstrap.servers": "kafka:29092"},
    )
    filtered_stream.add_sink(producer)

    env.execute("temperature-below-zero-filter")


if __name__ == "__main__":
    main()
