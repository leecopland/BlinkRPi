import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
import time
try:
    while 1:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt:
        GPIO.cleanup()
