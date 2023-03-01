import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 1, 1, 1, 1, 1, 1, 1]
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)
time.sleep(11)

GPIO.output(dac, 0)
GPIO.cleanup()