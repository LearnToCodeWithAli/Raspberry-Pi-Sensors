#Ali and Carlotta code KITT LEDS
#using a switch match case for one on at a time
#11/22/25 TikTok Live

import RPi.GPIO as GPIO #import library to send digital inputs and outputs
import time				#import time for the sleep functi9on
GPIO.setmode(GPIO.BCM)	#refer to pins by the broad comm chip (GPIOXX)	
GPIO.setwarnings(False)	#don't print out scripting warnings

GPIO.setup(16,GPIO.OUT)	#define pin 16 as an output
GPIO.setup(20,GPIO.OUT)	#define pin 20 as an output
GPIO.setup(21,GPIO.OUT) #define pin 21 as an output
print ("LED on")

blink = 1				#define global variable blink as a 1 to select match case
        
while True:				#run the code on the RPI for ever	
    match(blink):		#switch case to turn one LED on at a time
        case 1:
            GPIO.output(16,GPIO.HIGH)		#pin 16 LED HIGH, other 2 low
            GPIO.output(20,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)
            blink=2            
        case 2:
            GPIO.output(16,GPIO.LOW)		#pin 20 LED HIGH, other 2 low
            GPIO.output(20,GPIO.HIGH)
            GPIO.output(21,GPIO.LOW)
            blink=3 
        case 3:
            GPIO.output(16,GPIO.LOW)		#pin 21 LED HIGH, other 2 low
            GPIO.output(20,GPIO.LOW)
            GPIO.output(21,GPIO.HIGH)
            blink=1 
        
    time.sleep(1)		#sleep for one second
     
print ("LED off")



