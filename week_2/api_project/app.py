from flask import Flask, jsonify, request, g
import time
from kafka_producer import log_to_kafka

app = Flask(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    response_time = (time.time() - g.start_time) * 1000  # in milliseconds
    log_to_kafka(
        topic='logs',
        log_type='response',
        method=request.method,
        endpoint=request.path,
        status=response.status_code,
        response_time_ms=round(response_time, 2),
        message='Response recieved'
    )
    return response

@app.route('/')
def home():
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='GET',
        endpoint='/',
        response_time_ms=round(response_time, 2),
        message='Home page accessed'
    )
    return "Welcome to the API!"

@app.route('/api/resource', methods=['GET'])
def get_resource():
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='GET',
        endpoint='/api/resource',
        response_time_ms=round(response_time, 2),
        message='GET resource'
    )
    return jsonify({"message": "This is a GET resource!"})

@app.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='POST',
        endpoint='/api/resource',
        response_time_ms=round(response_time, 2),
        data=data,
        message='Resource created'
    )
    return jsonify({"message": "Resource created", "data": data}), 201

@app.route('/api/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.get_json()
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='PUT',
        endpoint=f'/api/resource/{id}',
        response_time_ms=round(response_time, 2),
        data=data,
        message=f'Resource {id} updated'
    )
    return jsonify({"message": f"Resource {id} updated", "data": data})

@app.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='DELETE',
        endpoint=f'/api/resource/{id}',
        response_time_ms=round(response_time, 2),
        message=f'Resource {id} deleted'
    )
    return jsonify({"message": f"Resource {id} deleted"})

@app.route('/api/status', methods=['GET'])
def api_status():
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='GET',
        endpoint='/api/status',
        response_time_ms=round(response_time, 2),
        message='Status checked'
    )
    return jsonify({"status": "API is running"})

@app.route('/api/query', methods=['GET'])
def query():
    query_param = request.args.get('q', 'No query provided')
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='requests',
        log_type='request',
        method='GET',
        endpoint='/api/query',
        response_time_ms=round(response_time, 2),
        query=query_param,
        message='Query received'
    )
    return jsonify({"query_received": query_param})

# Simulated error endpoints

@app.route('/api/error/network', methods=['GET'])
def simulate_network_error():
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='errors',
        log_type='error',
        method='GET',
        endpoint='/api/error/network',
        response_time_ms=round(response_time, 2),
        error_type='NetworkError',
        message='Simulated network issue'
    )
    return jsonify({"error": "Network connectivity problem"}), 503

@app.route('/api/error/database', methods=['GET'])
def simulate_database_error():
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='errors',
        log_type='error',
        method='GET',
        endpoint='/api/error/database',
        response_time_ms=round(response_time, 2),
        error_type='DatabaseError',
        message='Database operation failed'
    )
    return jsonify({"error": "Database query failed"}), 500

@app.route('/api/error/internal', methods=['GET'])
def simulate_internal_error():
    response_time = (time.time() - g.start_time) * 1000
    log_to_kafka(
        topic='errors',
        log_type='error',
        method='GET',
        endpoint='/api/error/internal',
        response_time_ms=round(response_time, 2),
        error_type='InternalError',
        message='Unexpected server error'
    )
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
