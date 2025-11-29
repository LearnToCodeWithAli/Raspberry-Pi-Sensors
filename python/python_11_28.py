import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # broadcom soc channel designation for a pin on a raspberry pi
# uses internal number scheme that's used by the chip itsel - google AI overview
GPIO.setwarnings(False)

red = 23
yellow = 24
green = 25

lights = [green, yellow, red]

for light in lights:
    GPIO.setup(light, GPIO.OUT)

print("LEDs set")

# GPIO.output(red,GPIO.HIGH)
# GPIO.output(yellow,GPIO.HIGH)
# GPIO.output(green,GPIO.HIGH)

current_light = input("What color is the light? ")

while current_light != "x":

    match (current_light):
        case "red":
            GPIO.output(red, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(red, GPIO.LOW)
        case "yellow":
            GPIO.output(yellow, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(yellow, GPIO.LOW)
        case "green":
            GPIO.output(green, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(green, GPIO.LOW)
    current_light = input("What color is the light? ")


print("LED off")
