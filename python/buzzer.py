# https://docs.sunfounder.com/projects/superkit-v2-pi/en/latest/Lesson_6_buzzer.html

import RPi.GPIO as GPIO
from time import sleep

# Disable warnings
GPIO.setwarnings(False)

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Set buzzer pin (Make sure your wire is on GPIO 13)
buzzer = 13
GPIO.setup(buzzer, GPIO.OUT)

try:
    while True:
        # Turn buzzer ON
        GPIO.output(buzzer, GPIO.HIGH)
        print("Beep")
        sleep(1.5) 

        # Turn buzzer OFF
        GPIO.output(buzzer, GPIO.LOW)
        print("No Beep")
        sleep(1.5)

except KeyboardInterrupt:
    # Cleans up the pins if you press Ctrl+C
    GPIO.cleanup()
