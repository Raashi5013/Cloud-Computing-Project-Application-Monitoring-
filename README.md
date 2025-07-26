Cloud Computing Mini Project
The Application Monitoring Dashboards project is a real-time log analytics system designed to monitor the health and performance of applications through structured logs and visual dashboards. The system collects logs from a RESTful Flask API, ingests them into Apache Kafka for streaming, processes them using a Kafka consumer, and stores the structured data in PostgreSQL. This log data is then visualized using Grafana, enabling developers and system administrators to gain insights into API usage, errors, and performance trends.

All components in the project—API server, Kafka producer and consumer, and the database—are containerized using Docker to ensure modular, portable, and cloud-ready deployment. The Kafka producer script captures logs like request events and errors from the API and pushes them to Kafka topics in real time. A request simulation script is also included to mimic traffic, allowing for stress testing and validation of the log pipeline.

The project visualizes metrics such as request count per API endpoint, response time patterns, most frequent errors, and real-time logs. These dashboards in Grafana offer operational observability and help in proactive system monitoring. The overall architecture follows a loosely coupled microservices design with message-based communication, making it scalable and fault-tolerant—key aspects of cloud-native systems.

This project reflects core cloud computing principles by combining containerization, decoupled services, real-time data streaming, centralized logging, and performance monitoring. .
