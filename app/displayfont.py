from datetime import date
import calendar

import board
import displayio

import adafruit_ili9341
from adafruit_rgb_display import color565
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

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

curr_date = date.today()
day_of_week = calendar.day_name[curr_date.weekday()]

# Set text, font, and color
text = day_of_week.upper()
font = bitmap_font.load_font(font_file)
color = 0xFFFFFF

# Create the tet label
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 90
text_area.y = 110
text_area.scale = 1

# Show it
display.show(text_area)

while True:
    pass
