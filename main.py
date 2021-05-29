# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
sensorPin = 4 # Broadcom pin 4

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(sensorPin, GPIO.IN) # Sensor pin set as output

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        status = GPIO.input(sensorPin)
        if(status):
            print "Please water the plant"
        else:
            print "Plant is doing fine"
        time.sleep(0.5)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
