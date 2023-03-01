import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

for i in range(1,24):
    GPIO.output(leds[i%8], 1)
    GPIO.output(leds[(i-1)%8], 0)
    time.sleep(0.2)

    GPIO.output(24, 0)

GPIO.cleanup()