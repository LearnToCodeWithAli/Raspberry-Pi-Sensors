# https://www.freva.com/how-to-connect-an-lcd-display-to-a-raspberry-pi/
# https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/overview use fr diagram
# non-normal behavior (cannot find i2c) https://learn.adafruit.com/scanning-i2c-addresses/raspberry-pi


# activate the venv before running or installing dependencies
# source raspberry-pi/bin/activate


from dependencies.lcd_api import LcdApi
from dependencies.i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("Great! It Works!")
lcd.move_to(3, 1)
lcd.putstr("freva.com")
