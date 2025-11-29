# Ali and Carlotta code a music machine
# using a buzzer, LCD, potentiometer, and sonar
# 11/28/25 TikTok Live

# run the code on the RPI one time like void setup() in Arduino
# include the necessary libraries
import RPi.GPIO as GPIO  # import library to send digital inputs and outputs
import time
import os
from song import song
from dependencies.notes import *


GPIO.setmode(GPIO.BCM)  # refer to pins by the broad comm chip (GPIOXX)
GPIO.setwarnings(False)  # don't print out scripting warnings

# declare variables and constants
songNo = 0  # sun number 0, song 1 or song 2
count = 0  # number of button presses
buzzerPin = 12  # PWM pin on RPI
trigPin = 21  # sonar trigger pin
echoPin = 20  # sonar echo pin\
joyPin = 7  # joystick button

GPIO.setup(buzzerPin, GPIO.OUT)  # define buzzer pin as output
GPIO.setup(trigPin, GPIO.OUT)  # define triger pin as output
GPIO.setup(echoPin, GPIO.IN)  # define echo pin as input
GPIO.setup(
    joyPin, GPIO.IN, pull_up_down=GPIO.PUD_UP
)  # define joystick pin as input with pull up resistor


def get_json(folder_path: str) -> tuple[str, ...]:
    return tuple(
        f"{folder_path}/{file}"
        for file in os.listdir(folder_path)
        if file.endswith(".json")
    )


# ---------------------------------------------------------

# songs melodies and note durations
melody = [
    notes.NOTE_A3,
    0,
    notes.NOTE_B3,
    0,
    notes.NOTE_C4,
    0,
    notes.NOTE_D4,
    0,
    notes.NOTE_E4,
    0,
    notes.NOTE_F4,
    0,
    notes.NOTE_G4,
    0,
]
noteDurations = [16, 32, 16, 32, 16, 32, 16, 32, 16, 32, 16, 32, 16, 32, 16, 32]
noteDurationsA = [16, 16, 16, 16, 8, 8, 8, 8]
noteDurationsB = [8, 8, 8, 8, 16, 16, 16, 16]


melody_3 = [
    (notes.NOTE_AS4, 8),
    (notes.NOTE_AS4, 8),
    (notes.NOTE_AS4, 8),
    (notes.NOTE_F5, 2),
    (notes.NOTE_C6, 2),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F6, 2),
    (notes.NOTE_C6, 4),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F6, 2),
    (notes.NOTE_C6, 4),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_G5, 2),
    (notes.NOTE_C5, 8),
    (notes.NOTE_C5, 8),
    (notes.NOTE_C5, 8),
    (notes.NOTE_F5, 2),
    (notes.NOTE_C6, 2),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F6, 2),
    (notes.NOTE_C6, 4),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F6, 2),
    (notes.NOTE_C6, 4),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_G5, 2),
    (notes.NOTE_C5, -8),
    (notes.NOTE_C5, 16),
    (notes.NOTE_D5, -4),
    (notes.NOTE_D5, 8),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F5, 8),
    (notes.NOTE_F5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 4),
    (notes.NOTE_D5, 8),
    (notes.NOTE_E5, 4),
    (notes.NOTE_C5, -8),
    (notes.NOTE_C5, 16),
    (notes.NOTE_D5, -4),
    (notes.NOTE_D5, 8),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F5, 8),
    (notes.NOTE_C6, -8),
    (notes.NOTE_G5, 16),
    (notes.NOTE_G5, 2),
    (notes.REST, 8),
    (notes.NOTE_C5, 8),
    (notes.NOTE_D5, -4),
    (notes.NOTE_D5, 8),
    (notes.NOTE_AS5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_F5, 8),
    (notes.NOTE_F5, 8),
    (notes.NOTE_G5, 8),
    (notes.NOTE_A5, 8),
    (notes.NOTE_G5, 4),
    (notes.NOTE_D5, 8),
    (notes.NOTE_E5, 4),
    (notes.NOTE_C6, -8),
    (notes.NOTE_C6, 16),
    (notes.NOTE_F6, 4),
    (notes.NOTE_DS6, 8),
    (notes.NOTE_CS6, 4),
    (notes.NOTE_C6, 8),
    (notes.NOTE_AS5, 4),
    (notes.NOTE_GS5, 8),
    (notes.NOTE_G5, 4),
    (notes.NOTE_F5, 8),
    (notes.NOTE_C6, 1),
]

# Tempo in beats per minute
tempo = 108
whole_note_duration = 60 / tempo * 4  # duration of a whole note


pause1 = 0.3
star_wars_pause = 0.005

# ----------------------------------------------------
song_list = get_song_files("./songs")


print("play intro song")
# play_song() #play starting song
play_star_wars()
time.sleep(1)  # wait 1 second


# run the code on the RPI forever like void loop() in Arduino
while True:
    pressed = GPIO.input(joyPin)
    print(GPIO.input(joyPin))
    if pressed == 0:
        count = count + 1
        time.sleep(0.1)  # debounce the button
    print("pressed = %2d" % (pressed))
    songNo = count % 3
    print("song number = %1d" % (songNo))
    if songNo == 1:
        play_song1()
        print("play song 1")
    elif songNo == 2:
        play_song2()
        print("play song 2")
    else:
        print("play nothing")
    time.sleep(0.1)  # wait 100 ms
