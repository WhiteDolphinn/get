import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

try:
    while True:
        value = input()

        if not(is_int(value)):
            print("Error.", value, "isn't a number.")
            break

        value = int(value)

        if value >= 256:
            print("Error.", value, "isn't a number from 0 to 255")
            break

        if value < 0:
            print("Error.", value, "isn't a number from 0 to 255")
            break
        
        print(3.3*value/256, "volts")
        GPIO.output(dac, dec2bin(value))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
