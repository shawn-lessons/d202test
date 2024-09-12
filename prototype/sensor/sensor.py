import time
import json
import random
import requests

url = 'http://127.0.0.1:5000/add_reading'  # Replace with your target URL

def send_json_data():
    while True:
        # Create the JSON data
        data = {
            "name": "test",  
            "number": random.randint(30, 50)  # simulate temperature
        }
        
        json_data = json.dumps(data)
        
        try:
            # POST request with the JSON data
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, json=data, headers=headers)
            print(f"Data sent: {data}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        
        time.sleep(30)

if __name__ == "__main__":
    send_json_data()
