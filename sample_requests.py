import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = 'http://{}:8080/tflite'.format(os.getenv('URL'))
# Define the data to be sent in the request body
data = {
    'xmin': 60,
    'xmax':2000,
    'label': 'hallo',
    'count': 1
}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    # Request was successful
    print('Response:', response.json())
else:
    # Request failed
    print('Error:', response.status_code)