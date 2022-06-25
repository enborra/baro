import time
import busio
import digitalio
import board
import terminalio
import displayio

from adafruit_rgb_display import color565
import adafruit_ili9341
from adafruit_display_text import label


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
    height=240
)

splash = displayio.Group()
display.show(splash)

while True:
    text = "Hello world"
    text_area = label.Label(
        terminalio.FONT,
        text=text,
        scale=1
    )
    text_area.x = 100
    text_area.y = 10

    splash.append(text_area)

    time.sleep(2)
