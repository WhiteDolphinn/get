import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = 0)

#GPIO.output(troyka, 0)

num_of_dots = 10000
sleep_time = 0.001

measured_data = [0] * num_of_dots

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def print_in_leds_2bit(value):
    GPIO.output(leds, 0)
    GPIO.output(leds, dec2bin(value))

def adc2():
    value = 0
    signal = 128
    delta = 64
    for i in range(8):
        GPIO.output(dac, dec2bin(signal))
        time.sleep(sleep_time)
        compvalue = GPIO.input(comp)

        if compvalue == 0:
            signal = signal - delta
            delta = int(delta / 2)
        else:
            signal = signal + delta
            value = value + 2*delta
            delta = int(delta / 2)

    #print(value)
    #print(dec2bin(value))
    #print(3.3*value/256, "volts")
    return value

try:

    while adc2() != 0:
        time.sleep(0.1)

    tm3 = time.time()

    for i in range(num_of_dots):
        value = adc2()
        measured_data[i] = value*3.3/256
        print_in_leds_2bit(value)
        print(i, value, 3.3*value/256)
        #time.sleep(0.005)

        if value > 250:
            GPIO.output(troyka, 1)

        if value == 62:
            GPIO.output(troyka, 0)

    measured_data_str = [str(item) for item in measured_data]

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(measured_data_str))

    with open("settings.txt", "w") as outfile:
        outfile.write("частота измерений ")
        outfile.write(str(1/sleep_time))
        outfile.write("\n частота дискретизации ")
        outfile.write(str(3.3/256))

    plt.plot(measured_data)
    plt.show()

    tm4 = time.time()
    print("time = ", tm4 - tm3)
    print("\n частота измерений ", 1/sleep_time)
    print("\n частота дискретизации", 3.3/256)


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

