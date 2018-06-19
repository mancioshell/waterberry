import configparser
import os

from waterberry.utils.logger import logger

config = configparser.ConfigParser()
config.read('/media/sf_Projects/waterberry/waterberry/config/waterberry.config')
raspberry = config.getboolean(os.environ['PLATFORM'], 'RPI_GPIO')

if raspberry:
    import Adafruit_CharLCD as LCD

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

class LCD:
    def __init__(self):
        if raspberry:
            self.lcd = LCD.Adafruit_CharLCDBackpack()

    def writeData(self, humidity, temperature):
        if raspberry:
            self.lcd.set_backlight(0)
            lcd.clear()
            lcd.message("{}u'\u2103'\n{}%".format(temperature, humidity))
        else:
            print "Writing {}u'\u2103'\n{}%".format(temperature, humidity)
