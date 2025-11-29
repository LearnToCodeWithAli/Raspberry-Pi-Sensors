#Ali and Carlotta code a music machine
#using a buzzer, LCD, potentiometer, and sonar
#11/28/25 TikTok Live

#run the code on the RPI one time like void setup() in Arduino
#include the necessary libraries
import RPi.GPIO as GPIO #import library to send digital inputs and outputs
import time #import time for the sleep functi9on
GPIO.setmode(GPIO.BCM) #refer to pins by the broad comm chip (GPIOXX)
GPIO.setwarnings(False) #don't print out scripting warnings

#declare variables and constants
songNo = 0 #sun number 0, song 1 or song 2
count = 0 #number of button presses
buzzerPin = 12 #PWM pin on RPI
trigPin = 21 #sonar trigger pin
echoPin = 20 #sonar echo pin\
joyPin = 7 #joystick button

GPIO.setup(buzzerPin,GPIO.OUT) #define buzzer pin as output
GPIO.setup(trigPin,GPIO.OUT) #define triger pin as output
GPIO.setup(echoPin,GPIO.IN) #define echo pin as input
GPIO.setup(joyPin,GPIO.IN, pull_up_down=GPIO.PUD_UP) #define joystick pin as input with pull up resistor

# Note frequencies
NOTE_FS4 = 370
NOTE_A4 = 440
NOTE_CS5 = 554
NOTE_D4 = 294
NOTE_CS4 = 277
NOTE_GS4 = 415
NOTE_G4 = 392
NOTE_E4 = 330
NOTE_C4 = 262
NOTE_E5 = 659
NOTE_B4 = 494
NOTE_D5 = 587
NOTE_B3 = 247
NOTE_F4 = 349
NOTE_AS4 = 466
NOTE_A5 = 880
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_FS5 = 740
NOTE_GS4 = 415
NOTE_DS4 = 311
NOTE_D4 = 294
NOTE_C4 = 262
NOTE_GS4 = 415

#songs melodies and note durations
melody = [NOTE_A3, 0,NOTE_B3, 0,NOTE_C4, 0, NOTE_D4, 0, NOTE_E4, 0, NOTE_F4, 0,NOTE_G4,0]
noteDurations = [16, 32,16, 32, 16, 32, 16, 32, 16, 32, 16,32, 16,32,16,32]
noteDurationsA = [16, 16, 16, 16, 8, 8, 8, 8]
noteDurationsB = [8, 8, 8, 8, 16, 16, 16, 16]

# Song 1
melody1 = [
  NOTE_FS4, NOTE_A4, NOTE_CS5, 0, NOTE_A4, 0, NOTE_FS4, NOTE_D4, NOTE_D4, NOTE_D4,
  0, 0, 0, NOTE_CS4, NOTE_D4, NOTE_FS4, NOTE_A4, NOTE_CS5, 0, NOTE_A4, 0, NOTE_FS4
]

noteDurations1 = [
  4, 8, 8, 8, 8, 8, 8, 8, 8, 8,
  8, 4, 8, 6, 8, 8, 8, 8, 8, 8
]

# Song 2
melody2 = [
  NOTE_C4, NOTE_D4, NOTE_F4, NOTE_D4, NOTE_A4, 0, NOTE_A4, NOTE_G4, 0,
  NOTE_C4, NOTE_D4, NOTE_F4, NOTE_D4, NOTE_G4, 0, NOTE_G4, NOTE_F4, 0
]

noteDurations2 = [
  1, 1, 1, 1, 1, 1, 4, 4, 2,
  1, 1, 1, 1, 1, 1, 4, 4, 2
]

# Tempo in beats per minute
tempo = 113
whole_note_duration = 60 / tempo * 4  # duration of a whole note

# Function to play a tone on the buzzer
def play_tone(frequency, duration):
    if frequency == 0:
        time.sleep(duration)
        return

    period = 1.0 / frequency
    cycles = int(duration / period)
    for i in range(cycles):
        GPIO.output(buzzerPin, True)
        time.sleep(period / 2)
        GPIO.output(buzzerPin, False)
        time.sleep(period / 2)

# Function to play the melody
def play_song():
    for i, note in enumerate(melody):
        duration = whole_note_duration / noteDurations[i]
        play_tone(note, duration)
        time.sleep(duration * 0.3)  # pause between notes


# Function to play the melody
def play_song1():
    for i, note in enumerate(melody1):
        duration = whole_note_duration / noteDurations1[i]
        play_tone(note, duration)
        time.sleep(duration * 0.3)  # pause between notes

# Function to play the melody
def play_song2():
    for i, note in enumerate(melody2):
        duration = whole_note_duration / noteDurations2[i]
        play_tone(note, duration)
        time.sleep(duration * 0.3)  # pause between notes
        
print ("play intro song")
play_song() #play starting song
time.sleep(1) #wait 1 second


#run the code on the RPI forever like void loop() in Arduino
while True:
    pressed = GPIO.input(joyPin)
    print(GPIO.input(joyPin)) 
    if (pressed==0):
        count = count+1
        time.sleep(0.1) #debounce the button
    print("pressed = %2d" % (pressed)) 
    songNo = count % 3
    print("song number = %1d" % (songNo)) 
    if (songNo == 1):
        play_song1()
        print ("play song 1") 
    elif (songNo == 2):
        play_song2()
        print ("play song 2")
    else:
        print("play nothing")
    time.sleep(0.1)#wait 100 ms