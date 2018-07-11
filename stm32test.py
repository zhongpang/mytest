#coding:utf-8

import time
import struct
import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
print(ser.port)
print(ser.baudrate)

#time.sleep(10)    

data = []
try:
    while True:
        print ("----------------------------------------------")
        datalen = ser.inWaiting()
        #print ("datalen:", datalen)
        if datalen !=0:
            #Read
            data = ser.read(datalen)
            ser.flushInput()    
            #print 'received:', data 
            bit_head = data[0]
            bit_funcd= data[1]
            bit_len  = data[2]
            int_CO2_H = int.from_bytes(data[3:4], byteorder='big')
            int_CO2_L = int.from_bytes(data[4:5], byteorder='big')
            co2 = int_CO2_H * 256 + int_CO2_L
            int_TVOC_H = int.from_bytes(data[5:6], byteorder='big')
            int_TVOC_L = int.from_bytes(data[6:7], byteorder='big')
            tvoc = (int_TVOC_H * 256 + int_TVOC_L)/10.0
            int_CH2O_H = int.from_bytes(data[7:8], byteorder='big')
            int_CH2O_L = int.from_bytes(data[8:9], byteorder='big')
            ch2o = (int_CH2O_H * 256 + int_CH2O_L)/10.0
            int_PM25_H = int.from_bytes(data[9:10], byteorder='big')
            int_PM25_L = int.from_bytes(data[10:11], byteorder='big')
            pm25 = int_PM25_H * 256 + int_PM25_L
            int_humidity_H = int.from_bytes(data[11:12], byteorder='big')
            int_humidity_L = int.from_bytes(data[12:13], byteorder='big')
            humidity = -6 + 125 * (int_humidity_H*256+int_humidity_L)/(2**16)
            int_temp_H = int.from_bytes(data[13:14], byteorder='big')
            int_temp_L = int.from_bytes(data[14:15], byteorder='big')
            temperature = -46.84 + 175.72 * (int_temp_H*256+int_temp_L)/(2**16)
            int_PM10_H = int.from_bytes(data[15:16], byteorder='big')
            int_PM10_L = int.from_bytes(data[16:17], byteorder='big')
            pm10 = int_PM10_H * 256 + int_PM10_L
            print("温度(0C)", temperature)
            print("湿度(%RH)", humidity)
            print("PM2.5(ug/m3):", pm25)
            print("PM10:", pm10)
            print("甲醛CH2O(ug/m3):", ch2o)
            print("总挥发性有机物TVOC(ug/m3):", tvoc)
            print("二氧化碳CO2(ppm):", co2)

            #print("reallen:%x, %d", data[2:3], int.from_bytes(data[2:3], byteorder='big'))

        time.sleep(1)    

except KeyboardInterrupt:
    if ser != None:
        ser.close()
 
if ser != None:
    ser.close()
