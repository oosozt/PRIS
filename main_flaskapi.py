from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

#todo: These blocks will be designed acc to main computer vision code. After training process this part will be changed.
# Define route for the API endpoint
@app.route('/', methods=['POST'])
def process_data():
    try:
        # Get the values of the variables from the JSON request
        data = request.json
        distance = data.get('distance')
        bbox0 = data.get('bbox0')
        bbox1 = data.get('bbox1')
        detected = data.get('detected')
        # Return a response in JSON format
        response = {
            'status': 'success',
            'message': 'Data received and processed successfully',
            'distance': distance,
            'bbox0': bbox0,
            'bbox1': bbox1,
            'detected': detected
        }
        print(response)
        return jsonify(response)
    except:
        print("Fehler")

@app.route('/tfminivalue', methods=['POST'])
def response_tfmini():
    # Get the values of the variables from the JSON request
    data = request.json
    tf_minidistance = data.get('distance')

    # Process the data as needed
    # You can perform computations, store the data in a database, etc.

    # Return a response in JSON format
    response_distance = {
        'status': 'success',
        'message': 'Data received and processed successfully',
        'distance': tf_minidistance
    }
    print(response_distance)
    return jsonify(response_distance)


if __name__ == '__main__':
    app.run(host=os.getenv("URL"), port=8080)
