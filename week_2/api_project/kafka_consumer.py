import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import json
from db import insert_log

# Retry loop for Kafka
while True:
    try:
        consumer = KafkaConsumer(
            'logs', 'requests', 'errors',
            bootstrap_servers='kafka:9092',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            group_id='log-consumer-group'
        )
        break  # Kafka connection successful
    except NoBrokersAvailable:
        print("Kafka not ready, retrying in 2 seconds...")
        time.sleep(2)

print("Kafka Consumer started...")

# Main loop to consume messages from Kafka
for message in consumer:
    topic = message.topic
    data = message.value
    print(f"Consumed from {topic}: {data}")

    # Insert log into the database
    try:
        insert_log(topic, data)
    except Exception as e:
        print(f"Error inserting into DB for topic {topic}: {e}")
