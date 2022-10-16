#include<Servo.h>
const int pingPin = 3; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 4; // Echo Pin of Ultrasonic Sensor

Servo servo1;
void setup(){
  servo1.attach(2);
  Serial.begin(9600);
}


void loop() {
   long duration, inches, cm;
   while(Serial.available()==0){}
   String data = Serial.readString();
   pinMode(pingPin, OUTPUT);
   delay(100);
   if(data == "1"){

       for(int i=50;i<135;i=i+10){
           servo1.write(i);
           delay(200);
           digitalWrite(pingPin, LOW);
           delayMicroseconds(2);
           digitalWrite(pingPin, HIGH);
           delayMicroseconds(10);
           digitalWrite(pingPin, LOW);
           pinMode(echoPin, INPUT);
           duration = pulseIn(echoPin, HIGH);
           cm = microsecondsToCentimeters(duration);
           if (cm <= 500){
            Serial.print(cm);
            Serial.print(",");
            Serial.print(i);
            Serial.println();
           }
           delay(100);
           if(i == 130){
              break;
            }
            }
   }
}
long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}