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

    _data = {
        'temp': None,
        'humidity': None,
        'barometric_pressure': None,
        'sea_level_pressure': None,
        'air_quality_small': None,
        'air_quality_medium': None,
        'air_quality_large': None
    }


    def __init__(self, *args, **kwargs):
        self.i2c = board.I2C()  # uses board.SCL and board.SDA

        self.tempSensor = adafruit_ahtx0.AHTx0( self.i2c )
        self.baroSensor = adafruit_bmp280.Adafruit_BMP280_I2C( self.i2c )
        self.baroSensor.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level
        self.airSensor = PM25_I2C( self.i2c, None )

    def refresh(self, *args, **kwargs):
        self._data['temp'] = (self.tempSensor.temperature.temperature*1.8)+32
        self._data['humidity'] = self.tempSensor.relative_humidity

        self._data['barometric_pressure'] = self.baroSensor.pressure
        self._data['altitude'] = self.baroSensor.altitude

        aq = self.airSensor.read()

        self._data['air_quality_small'] = aq['pm10 env']
        self._data['air_quality_medium'] = aq['pm25 env']
        self._data['air_quality_large'] = aq['pm100 env']


    def getStat(self, *args, **kwargs):

        pass

    def getDump(self, *args, **kwargs):
        o = {}

        try:
            o['temp'] = "Temp: %0.1f°F" % ((self.tempSensor.temperature*1.8)+32)
            o['humidity'] = "Humidity: %d" % self.tempSensor.relative_humidity
            o['pressure'] = "Pressure: %0.1f hPa" % self.baroSensor.pressure
            o['altitude'] = "Altitude: %d" % self.baroSensor.altitude
            o['aq'] = self.airSensor.read()

        except Exception as e:
            print(e)

        return o
