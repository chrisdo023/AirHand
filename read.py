import os, sys
import serial

ser = serial.Serial('/dev/ttyGS0', timeout=1, baudrate=115000)
ser.flushInput()

receive = False

while not receive:
	out = ser.readline().decode()
	if out !='': print(out); receive = True

print("done")
