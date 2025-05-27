import requests
import json

url = "https://hand-gesture-api-production.up.railway.app/predict"

# Prepare the data with exactly 63 float values
data = {
    "landmarks": [0.0] * 63
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response from the server
print("Status code:", response.status_code)
print("Response JSON:", response.json())
