# import time
# from time import strftime
# from datetime import date
# import calendar

import board

import adafruit_ahtx0
import adafruit_bmp280
from adafruit_pm25.i2c import PM25_I2C



# PM1
# Sources of PM1 include marine aerosol, soil erosion, volcanic eruptions, and
# forest fires. Other sources are burning fossil fuels, agricultural processes,
# cooking & cigarette smoke, emission from diesel-powered vehicles, power
# generation, industrial processes, and so on

# PM2.5
# Emission of particulate matter PM2.5 is either directly from a source
# (primary PM) or through the chemical reactions of gases such as oxides of
# sulfur (SOx), nitrogen oxides (NOx), organic compounds, etc. in the atmosphere
# (secondary PM). Simultaneously, the natural sources of particulate matter are
# wind-blown dust from open land, pollen, spores, mold, dirt, soil erosion, and
# forest fires.

# PM10
# Particulate matter PM10 is either directly emitted from a source (primary PM)
# or is formed through the chemical reactions of gases such as oxides of
# sulfur (SOx), nitrogen oxides (NOx), organic compounds, etc. in the atmosphere
# (secondary PM). Whereas, the natural sources of particulate matter are
# wind-blown dust from open land, pollen, spores, mold, dirt, soil erosion,
# and forest fires.


class Detector():
    tempSensor = None
    baroSensor = None
    airSensor = None

    _millibarToInchesOfMercury = 0.0295301



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
        self._data['temp'] = (self.tempSensor.temperature*1.8)+32
        self._data['humidity'] = self.tempSensor.relative_humidity

        self._data['barometric_pressure'] = self.baroSensor.pressure
        self._data['barometric_pressure_inches'] = self.baroSensor.pressure * self._millibarToInchesOfMercury
        self._data['altitude'] = self.baroSensor.altitude

        aq = self.airSensor.read()

        self._data['air_quality_small'] = aq['pm10 env']
        self._data['air_quality_medium'] = aq['pm25 env']
        self._data['air_quality_large'] = aq['pm100 env']


    def getStat(self, stat, *args, **kwargs):
        o = None

        if stat:
            o = self._data[ str(stat) ]

        return o
