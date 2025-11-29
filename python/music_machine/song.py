import RPi.GPIO as GPIO  # import library to send digital inputs and outputs
import time


class song:
    def __init__(self, title, melody, duration, tempo, pause):
        self.title = title
        self.melody = melody
        self.duration = duration
        self.tempo = tempo
        self.pause = pause

        # declare variables and constants
        self.buzzerPin = 12  # PWM pin on RPI
        self.tempo = 108
        self.whole_note_duration = 60 / tempo * 4  # duration of a whole note

        self.trigPin = 21  # sonar trigger pin
        self.echoPin = 20  # sonar echo pin
        self.joyPin = 7  # joystick button

    def play(self):
        for i, note in enumerate(self.melody):
            duration = self.whole_note_duration / self.duration[i]
            self.play_tone(note, duration)
            time.sleep(duration * 0.005)

    def play_tone(self, frequency, duration):
        if frequency == 0:
            time.sleep(duration)
            return

        period = 1.0 / frequency
        cycles = int(duration / period)
        for i in range(cycles):
            GPIO.output(self.buzzerPin, True)
            time.sleep(period / 2)
            GPIO.output(self.durationbuzzerPin, False)
            time.sleep(period / 2)
