import serial
import time
import requests
from dotenv import load_dotenv
import os
load_dotenv(".env")
ser = serial.Serial("/dev/ttyAMA0", 115200)
#todo: get distance value every 0.5 seconds in the process of servo motor
def getTFminiData():
    while True:
        count = ser.in_waiting
        time.sleep(0.2)
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()
            if recv[0] == 'Y' and recv[1] == 'Y': # 0x59 is 'Y'
                low = int(recv[2].encode('hex'), 16)
                high = int(recv[3].encode('hex'), 16)
                distance = low + high * 256
                print(distance)
                url = 'http://{}:8080/tfminivalue'.format(os.getenv('URL'))
                # Define the data to be sent in the request body
                data = {
                        'distance': '{}'.format(distance)
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

if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getTFminiData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()

