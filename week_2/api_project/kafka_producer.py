from kafka import KafkaProducer
import json
import time
from datetime import datetime

def create_producer():
    for i in range(5):
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("Connected to Kafka successfully.")
            return producer
        except Exception as e:
            print(f"Attempt {i+1}: Failed to connect to Kafka: {e}")
            time.sleep(5)
    raise Exception("Could not connect to Kafka after multiple attempts")

producer = create_producer()

def log_to_kafka(topic, log_type, method=None, endpoint=None, status=None,
                 response_time_ms=None, query=None, data=None, error_type=None, message=None):
    log_data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "log_type": log_type,
        "method": method or None,
        "endpoint": endpoint or None,
        "status": status,
        "response_time_ms": response_time_ms,
        "query": query,
        "data": data,
        "error_type": error_type,
        "message": message
    }

    try:
        producer.send(topic, value=log_data)
        producer.flush()
        print(f"Log sent to Kafka topic '{topic}':", log_data)
    except Exception as e:
        print("Error sending log to Kafka:", e)
