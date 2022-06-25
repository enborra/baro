import time
from time import strftime
from datetime import date
import calendar

import board
import displayio

import adafruit_ili9341
from adafruit_rgb_display import color565
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import adafruit_ahtx0
import adafruit_bmp280
from adafruit_pm25.i2c import PM25_I2C


from .models import Detector


i2c = board.I2C()  # uses board.SCL and board.SDA

tempSensor = adafruit_ahtx0.AHTx0(i2c)

baroSensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
baroSensor.sea_level_pressure = 1013.25 # change this to match the location's pressure (hPa) at sea level

airSensor = PM25_I2C(i2c, None)






displayio.release_displays()

spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25

display_bus = displayio.FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=board.D6
)

display = adafruit_ili9341.ILI9341(
    display_bus,
    width=320,
    height=240,
    rotation=180
)

splash = displayio.Group()

# Blank the screen

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)

display.show(splash)

font_large = bitmap_font.load_font("fonts/futura-medium-35.bdf")
font_small = bitmap_font.load_font("fonts/futura-medium-20.bdf")
cycle = True
cycle_count = 0

sensorData = None

def refreshData():
    o = {}

    try:
        o['temp'] = "Temp: %0.1f°F" % ((tempSensor.temperature*1.8)+32)
        o['humidity'] = "Humidity: %d" % tempSensor.relative_humidity
        o['pressure'] = "Pressure: %0.1f hPa" % baroSensor.pressure
        o['altitude'] = "Altitude: %d" % baroSensor.altitude

        o['aq'] = airSensor.read()

    except e as Exception:
        print(e)

    return o

sensorData = refreshData()


while True:
    color_bitmap = displayio.Bitmap(320, 240, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x000000
    bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
    splash.append(bg_sprite)

    t = strftime("%H:%M", time.localtime())
    ta = label.Label(font_small, text=t, color=0xaaaaaa)
    ta.x = 15
    ta.y = 15
    ta.scale = 1
    splash.append(ta)

    if cycle_count > 10:
        sensorData = refreshData()
        cycle_count = 0


    if (cycle_count % 2) == 0:
        t = sensorData['temp'] + "\n" + sensorData['humidity'] + "\n" + sensorData['pressure'] + "\n" + sensorData['altitude']
        ta = label.Label(font_small, text=t, color=0xffffff)
        ta.x = 40
        ta.y = 80
        ta.scale = 1
        splash.append(ta)

    else:
        t = "Air Quality"
        ta = label.Label(font_large, text=t, color=0xffffff)
        ta.x = 40
        ta.y = 80
        ta.scale = 1
        splash.append(ta)

        if sensorData['aq']:
            t = "Small dust: %d" % sensorData['aq']['pm10 env']
            t += "\n"
            t += "Medium dust: %d" % sensorData['aq']['pm25 env']
            t += "\n"
            t += "Big dust: %d" % sensorData['aq']['pm100 env']

        ta = label.Label(font_small, text=t, color=0xffffff)
        ta.x = 40
        ta.y = 120
        ta.scale = 1
        splash.append(ta)

    # display.show(text_area)
    # display.show(text_area_time)

    cycle_count = cycle_count + 1
    time.sleep(5)
