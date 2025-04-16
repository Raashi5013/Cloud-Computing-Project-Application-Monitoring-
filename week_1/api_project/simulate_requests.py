import requests
import time

def simulate_requests():
    base_url = 'http://flask-api:5000'

    # Simulate GET request
    response = requests.get(f'{base_url}/api/resource')
    print(f'GET /api/resource: {response.json()}')

    # Simulate POST request
    response = requests.post(f'{base_url}/api/resource', json={"name": "Test Resource"})
    print(f'POST /api/resource: {response.json()}')

    # Simulate PUT request
    response = requests.put(f'{base_url}/api/resource/1', json={"name": "Updated Resource"})
    print(f'PUT /api/resource/1: {response.json()}')

    # Simulate DELETE request
    response = requests.delete(f'{base_url}/api/resource/1')
    print(f'DELETE /api/resource/1: {response.json()}')

    # Simulate query
    response = requests.get(f'{base_url}/api/query', params={"q": "Hello, API!"})
    print(f'GET /api/query: {response.json()}')

if __name__ == "__main__":
    # Wait for the API to start up
    print("Waiting for Flask API to start...")
    time.sleep(10)
    
    # Run continuously
    while True:
        try:
            simulate_requests()
        except Exception as e:
            print(f"Error during request simulation: {e}")
        time.sleep(5)  # Simulate workload every 5 seconds