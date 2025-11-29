# Ali and Carlotta code KITT LEDS
# using a switch match case for one on at a time
# 11/22/25 TikTok Live

# run the code on the RPI one time
import RPi.GPIO as GPIO  # import library to send digital inputs and outputs
import time  # import time for the sleep functi9on

GPIO.setmode(GPIO.BCM)  # refer to pins by the broad comm chip (GPIOXX)
GPIO.setwarnings(False)  # don't print out scripting warnings
leds = [21, 20, 16, 12, 1, 7, 8, 25]  # define led pins
for led in leds:
    GPIO.setup(led, GPIO.OUT)  # define led pins as outputs


while True:  # run the code on the RPI forever
    for led in leds:  # turn LEDS on and off one at a time
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.1)
    for led in reversed(leds):  # turn LEDS on and off one at a time in reverse order
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.1)
