#coding:utf-8

import time
import struct
import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
print ser.port
print ser.baudrate

#time.sleep(10)    

data = []
try:
    while True:
        print 'serial test start ...' 
        datalen = ser.inWaiting()
        print 'datalen:', datalen 
        if datalen !=0:
            #Read
            data = ser.read(datalen)
            ser.flushInput()    
            #print 'received:', data 
            bit_head = data[0]
            bit_funcd= data[1]
            bit_len  = data[2]
            bit_temp_H = data[13]
            bit_temp_L = data[14]
            temperature = 0.0
            #temperature = -46.84 + 175.72 * (bit_temp_H*256+bit_temp_L)/(2^16)
            #temperature = bit_temp_H.hex()*256+bit_temp_L.hex()
            print 'datalen:', struct.unpack('<L', bytes(data[2:3]))

        time.sleep(1)    

except KeyboardInterrupt:
    if ser != None:
        ser.close()
 
if ser != None:
    ser.close()
