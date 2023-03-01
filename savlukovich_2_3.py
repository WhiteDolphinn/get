import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
i = 0

while True:
    GPIO.output(leds[i%8], GPIO.input(aux[i%8]))
    time.sleep(0.1)
    i = i + 1


#GPIO.cleanup()