import RPi.GPIO as GPIO
import time
import serial
ser = serial.Serial("/dev/ttyAMA0", 115200)
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
servo_count=50
servo1.start(0)
distances_collection=[]
def getTFminiData():
    tar =0
    while tar<11:
        #time.sleep(0.1)
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()
            # type(recv), 'str' in python2(recv[0] = 'Y'), 'bytes' in python3(recv[0] = 89)
            # type(recv[0]), 'str' in python2, 'int' in python3
            tar=tar+1
            if recv[0] == 0x59 and recv[1] == 0x59:     #python3
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                print('(', distance, ',', strength, ')')
                ser.reset_input_buffer()
                distances_collection.append(distance)
                print(distances_collection)

#            if recv[0] == 'Y' and recv[1] == 'Y':     #python2
#                lowD = int(recv[2].encode('hex'), 16)
#                highD = int(recv[3].encode('hex'), 16)
#                lowS = int(recv[4].encode('hex'), 16)
#                highS = int(recv[5].encode('hex'), 16)
#                distance = lowD + highD * 256
#                strength = lowS + highS * 256
#                print(distance, strength)
try:
    while servo_count<130:
        time.sleep(0.5)
        #Ask user for angle and turn servo to it
        #angle = float(input('Enter angle between 0 & 180: '))
        #servo1.ChangeDutyCycle(2+(angle/18))
        #time.sleep(0.5)
        #servo1.ChangeDutyCycle(0)
        start_angle=50
        last_angle=130
        step = 10
        for angle in range(start_angle, last_angle + 1, step):
            servo1.ChangeDutyCycle(2+(angle/18))
            getTFminiData()
            servo_count=servo_count+10
            time.sleep(0.5)
        print(min(distances_collection))
        try:
            if ser.is_open == False:
                ser.open()
        except KeyboardInterrupt:  # Ctrl+C
            if ser != None:
                ser.close()

finally:
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("degree 130 arrived")




