# https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson09_joystick.html
# https://github.com/keyestudio/KS3023-Keyestudio-Raspberry-Pi-Pico-37-in-1-Sensor-Kit-Raspberry-Pi/blob/master/Raspberry%20Pi/MicroPython/Pico_code_MicroPython/25.%20Joystick/joystick.py

import machine
import utime

B = machine.Pin(22, machine.Pin.IN)
X = machine.ADC(20)
Y = machine.ADC(21)
while True:
    B_value = B.value()
    X_value = X.read_u16()
    Y_value = Y.read_u16()
    print("button:", end=" ")
    print(B_value, end=" ")
    print("X:", end=" ")
    print(X_value, end=" ")
    print("Y:", end=" ")
    print(Y_value)
    utime.sleep(0.1)
