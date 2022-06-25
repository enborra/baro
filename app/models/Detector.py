import time
from time import strftime
from datetime import date
import calendar

import board

import adafruit_ili9341
from adafruit_rgb_display import color565
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import adafruit_ahtx0
import adafruit_bmp280
from adafruit_pm25.i2c import PM25_I2C


class Detector():
    tempSensor = None
    baroSensor = None
    airSensor = None


    def __init__(self, *args, **kwargs):
        self.i2c = board.I2C()  # uses board.SCL and board.SDA

        self.tempSensor = adafruit_ahtx0.AHTx0( self.i2c )
        self.baroSensor = adafruit_bmp280.Adafruit_BMP280_I2C( self.i2c )
        self.baroSensor.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level
        self.airSensor = PM25_I2C( self.i2c, None )


    def getStat(self, *args, **kwargs):

        pass

    def getDump(self, *args, **kwargs):
        o = {}

        try:
            o['temp'] = "Temp: %0.1f°F" % ((tempSensor.temperature*1.8)+32)
            o['humidity'] = "Humidity: %d" % tempSensor.relative_humidity
            o['pressure'] = "Pressure: %0.1f hPa" % baroSensor.pressure
            o['altitude'] = "Altitude: %d" % baroSensor.altitude

            o['aq'] = airSensor.read()

        except Exception as e:
            print(e)

        return o
