#coding:utf-8

import time
import RPi.GPIO as GPIO
import serial

#set control
channel =18
 
GPIO.setmode(GPIO.BCM)
time.sleep(1)
GPIO.setup(channel, GPIO.OUT)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)

ser = serial.Serial("/dev/ttyAMA0", 9600)
data = []
try:
    #while True:
    print("serial test start ...")
    datalen = ser.inWaiting()
    if datalen !=0:
        #Read
        data = ser.read(datalen)
        print("received:", data)

except KeyboardInterrupt:
    if ser != None:
        ser.close()
    GPIO.cleanup()
 
