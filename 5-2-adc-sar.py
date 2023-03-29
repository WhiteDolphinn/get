import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    for value in range(256):
        GPIO.output(dac, dec2bin(value))
        time.sleep(0.0005)
        compvalue = GPIO.input(comp)
        if compvalue == 0:
            print(value)
            print(dec2bin(value))
            print(3.3*value/256 ,"volts")
            return value

def adc2():
    value = 0
    signal = 128
    delta = 64
    for i in range(8):
        GPIO.output(dac, dec2bin(signal))
        time.sleep(0.0005)
        compvalue = GPIO.input(comp)

        if compvalue == 0:
            signal = signal - delta
            delta = int(delta / 2)
        else:
            signal = signal + delta
            value = value + 2*delta
            delta = int(delta / 2)

    print(value)
    print(dec2bin(value))
    print(3.3*value/256, "volts")
    #return value


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

try:
    while True:
        tm3 = time.time()
        value = adc()
        tm4 = time.time()
        print("adc() time = ", tm4 - tm3)

        tm1 = time.time()
        adc2()
        tm2 = time.time()
        print("adc2() time = ", tm2 - tm1)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
