import RPi.GPIO as GPIO
import time

led = 18
red = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(red,GPIO.IN)

try:
    while True:
        if GPIO.input(red) == True:
            GPIO.output(led,True)
        else:
            GPIO.output(led,False)
except KeyboardInterrupt:
    print("push ctrl C")
    GPIO.cleanup()