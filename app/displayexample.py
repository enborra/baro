# import time
# import busio
# import digitalio
# # from board import SCK, MOSI, MISO, D2, D3
# from board import SCK, MOSI, MISO, CE0, D24, D25
#
# from adafruit_rgb_display import color565
# import adafruit_rgb_display.ili9341 as ili9341
#
#
# # Configuration for CS and DC pins:
# # CS_PIN = D2
# # DC_PIN = D3
# CS_PIN = CE0
# DC_PIN = D25
#
# # Setup SPI bus using hardware SPI:
# spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)
#
# # Create the ILI9341 display:
# display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(CS_PIN),
#                           dc=digitalio.DigitalInOut(DC_PIN))
#
# # Main loop:
# while True:
#     # Clear the display
#     display.fill(0)
#     # Draw a red pixel in the center.
#     display.pixel(0, 0, color565(255, 0, 0))
#     # Pause 2 seconds.
#     time.sleep(2)
#     # Clear the screen blue.
#     display.fill(color565(0, 0, 255))
#     # Pause 2 seconds.
#     time.sleep(2)

import time
import busio
import digitalio
import board
from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341

spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(board.CE0),
    dc=digitalio.DigitalInOut(board.D25))


while True:
    display.fill(color565(0x00, 0x00, 0x00))
    display.fill_circle(100, 120, 20, color565(0xff, 0xff, 0xff))
    display.fill_circle(100, 220, 20, color565(0xff, 0xff, 0xff))

    time.sleep(2)

    display.fill(color565(0x00, 0x00, 0x00))

    time.sleep(2)
