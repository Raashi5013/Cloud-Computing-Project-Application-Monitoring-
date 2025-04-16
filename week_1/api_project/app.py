from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/api/resource', methods=['GET'])
def get_resource():
    return jsonify({"message": "This is a GET resource!"})

@app.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    return jsonify({"message": "Resource created", "data": data}), 201

@app.route('/api/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.get_json()
    return jsonify({"message": f"Resource {id} updated", "data": data})

@app.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    return jsonify({"message": f"Resource {id} deleted"})

@app.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({"status": "API is running"})

@app.route('/api/query', methods=['GET'])
def query():
    query_param = request.args.get('q', 'No query provided')
    return jsonify({"query_received": query_param})

if __name__ == "__main__":
    # Changed to 0.0.0.0 to allow connections from other containers
    app.run(debug=True, host='0.0.0.0')