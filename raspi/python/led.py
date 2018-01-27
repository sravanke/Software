# program to blink an led  every 3 seconds
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
while 1:
	print "LED on"
	GPIO.output(2,GPIO.HIGH)
	time.sleep(3)
	print "LED off"
	GPIO.output(2,GPIO.LOW)
	time.sleep(3)

