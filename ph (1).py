import RPi.GPIO as GPIO
import time
import os
import sys
import json
import requests # importing the requests library
from json_tricks import dumps
from time import sleep 
import serial

GPIO.setmode(GPIO.BOARD)  # Configures how we are describing our pin numbering
ser = serial.Serial('/dev/ttyACM0', 9600)
API_ENDPOINT="https://geoffish.herokuapp.com/api/post_ph/"





    
print ("PH measurement in progress")
while True:
    ph=ser.readline()
    print(ph)
    time.sleep(5)
    r=requests.post(url=API_ENDPOINT, data={'data':ph})
    print (r)
    ser.close()
    time.sleep(1)         
    ser.open()
  

   


