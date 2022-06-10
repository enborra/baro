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

    if cycle:
        temp = "Temp: %d°F" % ((tempSensor.temperature*1.8)+32)
        humidity = "Humidity: %d" % tempSensor.relative_humidity
        pressure = "hPa pressure: %d" % baroSensor.pressure
        altitude = "Altitude: %d" % baroSensor.altitude

        t = temp + "\n" + humidity + "\n" + pressure + "\n" + altitude
        ta = label.Label(font_small, text=t, color=0xffffff)
        ta.x = 40
        ta.y = 80
        ta.scale = 1
        splash.append(ta)

        cycle = False

    else:
        aq = airSensor.read()
        t = "Air quality: "
        t += "\n\n"
        t += "pm1: %d" % aq['pm10 standard']
        t += "\n"
        t += "pm2.5: %d" % aq['pm25 standard']
        t += "\n"
        t += "pm10: %d" % aq['pm100 standard']

        ta = label.Label(font_small, text=t, color=0xffffff)
        ta.x = 40
        ta.y = 80
        ta.scale = 1
        splash.append(ta)

        cycle = True

    # display.show(text_area)
    # display.show(text_area_time)

    time.sleep(60)
