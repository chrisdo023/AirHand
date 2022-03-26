import time

counter = 0
volume = 0
while True:
	val = raw_input("Cmd: ")
	if val == "I":
		volume = volume + 5
        elif val == "D":
                volume = volume - 5

        cmd = 'set volume output volume ' + str(volume)

	# rfcomm0 is used for bluetooth
#	with open('/dev/rfcomm0', 'w', 1) as f:

	# ttyGS0 is used for usb serial port
	with open('/dev/ttyGS0', 'w', 1) as f:
		f.write(cmd)
#		f.write('Counter: ' + str(counter) + '\n')
#		f.write('Increase')
#	counter += 1


#with open('/dev/ttyGS0', 'w', 1) as f:
#	f.write('Increase')
#time.sleep(1)

