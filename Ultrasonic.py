import time
import RPi.GPIO as GPIO

class Ultrasonic(object):
	#distance = -1
	
	GPIO_TRIGGER = 23
	GPIO_ECHO    = 24
	
	def __init__(self):
		print "Starting sensor..."
		
		GPIO.setmode(GPIO.BCM)

		# Set pins as output and input
		GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
		GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

		# Set trigger to False (Low)
		GPIO.output(GPIO_TRIGGER, False)
		
		# Wrap main content in a try block so we can
		# catch the user pressing CTRL-C and run the
		# GPIO cleanup function. This will also prevent
		# the user seeing lots of unnecessary error
		# messages.
		try:

		  while True:

			#distance = measure_average()
			#print "Distance : %.1f" % distance
			print "ok"
			time.sleep(1)

		except KeyboardInterrupt:
		  # User pressed CTRL-C
		  # Reset GPIO settings
		  GPIO.cleanup()
		
		
	


sensor = Ultrasonic()
