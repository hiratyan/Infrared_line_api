import api_line
import RPi.GPIO as GPIO
from time import sleep

red = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.IN)

try:
    while True:
        if GPIO.input(red) == True:
            api_line.send_line_notify("泥棒が入ってきました")
            sleep(10)
        else:
            pass
except KeyboardInterrupt:
    print("push ctrl C")
    GPIO.cleanup()