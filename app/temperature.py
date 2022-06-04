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


i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

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
display.show(splash)

font_large = bitmap_font.load_font("fonts/futura-medium-35.bdf")
font_small = bitmap_font.load_font("fonts/futura-medium-20.bdf")

while True:
    temp = "Temp: %d°F" % ((sensor.temperature*1.8)+32)
    humidity = "Humidity: %d" % sensor.relative_humidity

    text = temp + "\n" + humidity
    text_area = label.Label(font_large, text=text, color=0xffffff)
    text_area.x = 40
    text_area.y = 80
    text_area.scale = 1
    splash.append(text_area)

    text = strftime("%H:%M", time.localtime())
    text_area_time = label.Label(font_small, text=text, color=0xaaaaaa)
    text_area_time.x = 15
    text_area_time.y = 15
    text_area.scale = 1
    splash.append(text_area_time)

    # display.show(text_area)
    # display.show(text_area_time)

    time.sleep(60)
