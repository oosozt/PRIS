from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import json

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

@app.route('/tflite',methods=['POST'])
def tensorflow_recognizer():
    data = request.json
    xmin = data.get('xmin')
    xmax = data.get('ymin')
    label=data.get('label')
    count=data.get('count')

    # Process the data as needed
    # You can perform computations, store the data in a database, etc.

    # Return a response in JSON format
    response_tensorflow = {
        "status": "success",
        "message": "Data received and processed successfully",
        "xmin": xmin,
        "label":label,
        "xmax":xmax,
        "count": count

    }
    # Open a file for writing
    with open("object.json", "w") as f:
        # Serialize the object to JSON and write it to the file
        json.dump(response_tensorflow, f)

    print("Object written to file.")
    print(response_tensorflow)
    return jsonify(response_tensorflow)

# @app.route('/mapdata',methods=['GET'])
# def data_request():



if __name__ == '__main__':
    app.run(host=os.getenv("URL"), port=8080)
