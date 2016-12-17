import pygame
from pygame.locals import *
import sys
import subprocess
import logging
import time
import RPi.GPIO as GPIO

#GPIO pins
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

VIDEO_LENGHT = 45
DISTANCE_THRESHOLD =40
#state
IDLE = 0
PLAYING = 1

#DEBUG = False

def init_sensor():
	
	GPIO.cleanup()
	
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
	try:
		GPIO.output(GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER, False)

		time.sleep(0.00006)

		start = time.time()
		
		reties = 0

		while GPIO.input(GPIO_ECHO)==0:
			reties += 1
			if reties > 1000:
				return 100
			start = time.time()

		stop = time.time()

		while GPIO.input(GPIO_ECHO)==1:
			stop = time.time()

		elapsed = stop-start
		distance = (elapsed * 34300)/2
		return distance
	except:
		print "Error measuring"
		measure()

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
	
	DEBUG = False
	
	pygame.init()
	screen = pygame.display.set_mode((1280, 720))
	pygame.display.set_caption("Meeting Place")
	pygame.display.toggle_fullscreen()
	pygame.mouse.set_visible(False)
	
	logo = pygame.image.load("logo.png")
	logo = pygame.transform.rotate(logo, 90)
	
	screen.blit(logo, (200,100))
	
	font = pygame.font.SysFont("monospace", 24)	

	print "Starting Meeting Place"
	
	init_sensor()
	
	time.sleep(2)
	
	state = IDLE
	
	try:
		while True:
			
			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GPIO.cleanup()
						sys.exit()
					if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						GPIO.cleanup()
						sys.exit()
					if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
						#subprocess.call(['omxplayer', 'video.mp4'])
						video = subprocess.Popen(['omxplayer', '--win', '200 0 1280 720', 'video.mp4'])
					if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
							DEBUG = not DEBUG
			
			time.sleep(1)
					
			if state == IDLE:
				pygame.display.flip()
				screen.fill((0,0,0))
				
				#render logo
				logo = pygame.image.load("logo.png")
				logo = pygame.transform.rotate(logo, 90)
				screen.blit(logo, (200,100))	
				
				distance = measure_average()
				
				if DEBUG == True:
					distance_indicator = font.render("Distance: %.1f" % distance, 1, (255,255,255))
					distance_indicator = pygame.transform.rotate(distance_indicator, 90)
					screen.blit(distance_indicator, (400, 120))
					#print "Distance : %.1f" % distance
				
				if distance <= DISTANCE_THRESHOLD:
					state = PLAYING
					#video = subprocess.Popen(['omxplayer', 'video.mp4'])
					
					time.sleep(VIDEO_LENGHT)
					
					state = IDLE
					
					#video.kill()
					#video.terminate()
										
					init_sensor()
					
					time.sleep(2)
					print "Thanks!"
					
			pygame.display.update()	
			
						
	except KeyboardInterrupt:
		# User pressed CTRL-C
		# Reset GPIO settings
		GPIO.cleanup()
		sys.exit()

if __name__ == "__main__":
    main()

#subprocess.call(['omxplayer', 'reel.mp4'])
