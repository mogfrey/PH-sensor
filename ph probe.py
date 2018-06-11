import RPi.GPIO as GPIO
import time
import json
import requests # importing the requests library
from json_tricks import dumps
from time import sleep 
import serial

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
OutputPins = [5]
ser = serial.Serial('/dev/ttyACM0', 9600)
# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=5)


def sms_warning():
    time.sleep(1)
    port.write(('AT'+'\r\n').encode())
    time.sleep(1)
    port.write(('ATE0'+'\r\n').encode())      # Disable the Echo
    time.sleep(1)
    port.write(('AT+CMGF=1'+'\r\n').encode())  # Select Message format as Text mode 
    time.sleep(1)
    port.write(('AT+CNMI=2,1,0,0,0'+'\r\n').encode())   # New SMS Message Indications
    time.sleep(1)
    # Sending a message to a particular Number
         
    port.write(('AT+CMGS="0726309019"'+'\r\n').encode())
    #rcv = port.read(10)
    #print (rcv)
    
    time.sleep(1)
    
def call_warning():
    port.write(('ATD0726309019;'+'\r').encode())


while True:
    ph=ser.readline()
    phint=int.from_bytes(ph,byteorder='big',signed=False)
    time.sleep(5)


    if (phint)<= 6:
        print("WARNING !! water too acidic !!")
        
        call_warning()
        sms_warning()

        print("correction in progress")

        for i in OutputPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
        sleep(5)
        for i in OutputPins:
            GPIO.output(i, True)
        sleep(5)
        


        
        port.write(('WARNING !! water too acidic. correction in progress!!'+'\r').encode())  # Message
        time.sleep(1)
        port.write(("\x1A").encode()) # Enable to send SMS
        time.sleep(1)
        
        
        time.sleep(120)


    elif (phint)>= 8:
        print("WARNING !! water too alkaline !!")
        
        call_warning()
        sms_warning()

        print("correction in progress")

        for i in OutputPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, False)
        sleep(5)
        for i in OutputPins:
            GPIO.output(i, True)
        sleep(5)
        


        
        port.write(('WARNING !! water too alkaline. correction in progress!!'+'\r').encode())  # Message
        time.sleep(1)
        port.write(("\x1A").encode()) # Enable to send SMS
        time.sleep(1)
        
        
        time.sleep(120)
     


        
    
    
