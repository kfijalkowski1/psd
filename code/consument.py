import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        group_id='my-consumer-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        print(message.value)
