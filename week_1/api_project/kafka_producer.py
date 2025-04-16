from kafka import KafkaProducer
import json
import time

def create_producer():
    # Add retry mechanism
    for i in range(5):
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("Successfully connected to Kafka")
            return producer
        except Exception as e:
            print(f"Failed to connect to Kafka (attempt {i+1}/5): {e}")
            if i < 4:  # Don't sleep on the last attempt
                time.sleep(10)
    
    raise Exception("Could not connect to Kafka after multiple attempts")

def send_log_to_kafka(producer, log_data):
    try:
        producer.send('logs', value=log_data)
        producer.flush()
        print("Log sent to Kafka:", log_data)
    except Exception as e:
        print(f"Error sending log to Kafka: {e}")

# Simulate log generation
def generate_logs():
    logs = [
        {"level": "INFO", "message": "API started successfully"},
        {"level": "ERROR", "message": "Error processing request"},
        {"level": "INFO", "message": "Resource created"}
    ]
    
    # Wait for Kafka to start up
    print("Waiting for Kafka to start...")
    time.sleep(30)
    
    producer = create_producer()
    
    while True:
        for log in logs:
            send_log_to_kafka(producer, log)
            time.sleep(5)  # Simulate log generation every 5 seconds

if __name__ == "__main__":
    generate_logs()