import pygame
from pygame.locals import *
import sys
import subprocess
import logging
import time
import RPi.GPIO as GPIO

GPIO_TRIGGER = 23
GPIO_ECHO    = 24

def init_sensor():
	GPIO.setmode(GPIO.BCM)

	# Define GPIO to use on Pi

	print "Ultrasonic Measurement"

	# Set pins as output and input
	GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
	GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance
	
def main():
	pygame.init()
	screen = pygame.display.set_mode((1280, 720))
	pygame.display.set_caption("Meeting Place")
	pygame.display.toggle_fullscreen()
	pygame.mouse.set_visible(False)
	
	logo = pygame.image.load("logo.png")
	#logo = pygame.transform.scale(logo, (200,188))
	logo = pygame.transform.rotate(logo, 90)
	screen.blit(logo, (100,100))

	print"Starting Meeting Place"
	
	init_sensor()
	
	time.sleep(2)
	
	try:
		while True:
			pygame.display.flip()
			distance = measure_average()
			#print "Distance : %.1f" % distance
			
			#time.sleep(1)
			
			if distance <= 5:
				#print "SHOOOT"
				subprocess.call(['omxplayer', 'video.mp4'])
				#time.sleep(10)
			
			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GPIO.cleanup()
						sys.exit()
					if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						GPIO.cleanup()
						sys.exit()
					if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
						subprocess.call(['omxplayer', 'video.mp4'])
	except KeyboardInterrupt:
		# User pressed CTRL-C
		# Reset GPIO settings
		GPIO.cleanup()
		sys.exit()

if __name__ == "__main__":
    main()

#subprocess.call(['omxplayer', 'reel.mp4'])
