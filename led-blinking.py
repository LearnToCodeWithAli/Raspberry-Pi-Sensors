import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
print ("LED on")

count = 5

blink = True
while True:
    
    if blink:
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        blink = not blink
    else:
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        blink = not blink
        
    time.sleep(1)
    count -= 1
    
    
print ("LED off")
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.LOW)

