# https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson22_touch_sensor.html
# This code will turn on the LEDs when the touch sensor is pushed.
# S stands for serial and should be connected to the corresponding GPIO pin and a resistor greater than 1M ohms
# VCC can be connected to 3.3V, ground must be connected to ground

from gpiozero import Button
from signal import pause
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


# Function called when the sensor is touched
def touched():
    # Print a message indicating the sensor is touched
    print("Touched!")
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)


# Function called when the sensor is not touched
def not_touched():
    # Print a message indicating the sensor is not touched
    print("Not touched!")
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)


# Initialize a Button object for the touch sensor
# GPIO 17: pin connected to the sensor
# pull_up=None: disable internal pull-up/pull-down resistors
# active_state=True: high voltage is considered the active state
touch_sensor = Button(13, pull_up=None, active_state=True)

# Assign functions to sensor events
touch_sensor.when_pressed = touched
touch_sensor.when_released = not_touched

pause()  # Keep the program running to detect touch events
