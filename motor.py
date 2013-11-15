##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Setup for motor 1
#for motor 2 change to pins 22 and 23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
#Now loop forever turning one direction for 5 seconds, then the other
while (True):
	GPIO.output(17, 1)
	time.sleep(5);
	GPIO.output(17, 0)
	time.sleep(1);
	GPIO.output(18, 1);
	time.sleep(5);
	GPIO.output(18, 0);
	time.sleep(1);
#End
GPIO.cleanup()
