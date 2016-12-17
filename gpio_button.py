import pygame
from pygame.locals import *
import sys
import subprocess
import logging
import time
import RPi.GPIO as GPIO

SENSOR = 24
LED = 23

def main():
	print "Sensors Testing"
		
	GPIO.setmode(GPIO.BCM)
	
	# Set pins as output and input
	GPIO.setup(LED,GPIO.OUT)
	GPIO.setup(SENSOR,GPIO.IN)

	# Set trigger to False (Low)
	GPIO.output(LED, False)
	
	timer = 0
	
	time.sleep(1)
	#GPIO.output(LED, True)
	#GPIO.output(SENSOR, False)
	
	try:
		while True:
			time.sleep(0.1)
			timer += 1
			ir_sensor()
			#print "Timer: %.1f" % timer
			
			
	except KeyboardInterrupt:
		# User pressed CTRL-C
		GPIO.cleanup()
		sys.exit()
		
def ir_sensor():
	retries = 0
	
	#print "Sensor: ", GPIO.input(SENSOR)
	button = GPIO.input(SENSOR)
	
	if button == 0:
		print "Clear"
		GPIO.output(LED, False)
	else:
		GPIO.output(LED, True)
		print "Some thing on the road!"

	
if __name__ == "__main__":
    main()
