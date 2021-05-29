# External module imports
import RPi.GPIO as GPIO
import time
import boto3
import os
print(os.environ)
# Pin Definitons:
sensorPin = 4 # Broadcom pin 4

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(sensorPin, GPIO.IN) # Sensor pin set as output

s3 = boto3.resource(
    's3',
    region_name='us-west-2',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        status = GPIO.input(sensorPin)
        if(status):
            print("Please water the plant")
            content="{\"sensor\":true}"
        else:
            print("Plant is doing fine")
            content="{\"sensor\":false}"
        s3.Object('jion-public', "sensor"+str(sensorPin)+".json").put(Body=content)
        time.sleep(60*60) #once every hour
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
