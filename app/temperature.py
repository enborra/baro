import time
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


font_file = "fonts/futura-medium-35.bdf"

font = bitmap_font.load_font(font_file)

while True:
    temp = "Temp: %d°F" % ((sensor.temperature*1.8)+32)
    humidity = "Humidity: %d" % sensor.relative_humidity

    text = temp
    font = bitmap_font.load_font(font_file)
    color = 0xFFFFFF

    # Create the tet label
    text_area = label.Label(font, text=text, color=color)

    # Set the location
    text_area.x = 40
    text_area.y = 110
    text_area.scale = 1

    # Show it
    display.show(text_area)

    time.sleep(10)
