#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Author : Matt Hawkins
# Date   : 28/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO
<<<<<<< HEAD

# -----------------------
# Define some functions
# -----------------------

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

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

print "Ultrasonic Measurement"

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

    distance = measure_average()
    print "Distance : %.1f" % distance
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
=======
 
GPIO.setmode(GPIO.BOARD) #Queremos usar la numeracion de la placa
 
#Definimos los dos pines del sensor que hemos conectado: Trigger y Echo
Trig = 11
Echo = 13
 
#Hay que configurar ambos pines del HC-SR04
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
 
#Para leer la distancia del sensor al objeto, creamos una funcion
def detectarObstaculo():
 
   GPIO.output(Trig, False) #apagamos el pin Trig
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(Trig, True) #encendemos el pin Trig
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(Trig, False) #y lo volvemos a apagar
 
  #empezaremos a contar el tiempo cuando el pin Echo se encienda
   while GPIO.input(Echo) == 0:
      start = time.time()
 
   while GPIO.input(Echo) == 1:
      end = time.time()
      
   print "%.2f" %start
 
   #La duracion del pulso del pin Echo sera la diferencia entre
   #el tiempo de inicio y el final
   
   #duracion = end-start
 
   #Este tiempo viene dado en segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   #de la documentacion
   
   #duracion = duracion*10**6
   #medida = duracion/58 #hay que dividir por la constante que pone en la documentacion, nos dara la distancia en cm
 
   #print "%.2f" %medida #por ultimo, vamos a mostrar el resultado por pantalla
 
	
#Bucle principal del programa, lee el sensor. Se sale con CTRL+C
while True:
   try:
      detectarObstaculo()
   except KeyboardInterrupt:
      break
 
#por ultimo hay que restablecer los pines GPIO
print "Limpiando..."
GPIO.cleanup()
print "Acabado."
>>>>>>> 892f041c9ad1eb9863b6cbaafeecd37a246f2025
