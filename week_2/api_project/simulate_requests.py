import requests
import time

def simulate_requests():
    base_url = 'http://flask-api:5000'

    try:
        print("Simulating API calls...")

        # Standard routes
        response = requests.get(f'{base_url}/api/resource')
        print(f'GET /api/resource: {response.json()}')

        response = requests.post(f'{base_url}/api/resource', json={"name": "Test Resource"})
        print(f'POST /api/resource: {response.json()}')

        response = requests.put(f'{base_url}/api/resource/1', json={"name": "Updated Resource"})
        print(f'PUT /api/resource/1: {response.json()}')

        response = requests.delete(f'{base_url}/api/resource/1')
        print(f'DELETE /api/resource/1: {response.json()}')

        response = requests.get(f'{base_url}/api/query', params={"q": "Hello, API!"})
        print(f'GET /api/query: {response.json()}')

        # Separated error simulations
        error_endpoints = [
            "/api/error/network",
            "/api/error/validation",
            "/api/error/database"
        ]
        for endpoint in error_endpoints:
            response = requests.get(f'{base_url}{endpoint}')
            print(f'{endpoint}: {response.json()}')

    except Exception as e:
        print(f"Error during request simulation: {e}")

if __name__ == "__main__":
    print("Waiting for Flask API to start...")
    time.sleep(10)

    while True:
        simulate_requests()
        time.sleep(5)
