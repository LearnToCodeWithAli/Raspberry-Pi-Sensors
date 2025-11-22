import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
print ("LED on")

count = 5

blink = 1
        
while True:
    match(blink):
    case 1:
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        blink=2            
    case 2:
        GPIO.output(16,GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        blink=3 
    case 3:
        GPIO.output(16,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        blink=1 
        
    time.sleep(1)
    count -= 1
    
    
print ("LED off")
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.LOW)


