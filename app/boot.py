import sys
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

from models.Detector import Detector


if __name__ == "__main__":
    d = Detector()
    d.refresh()

    displayio.release_displays()

    spi = board.SPI()
    tft_cs = board.CE0
    tft_dc = board.D25

    display_bus = displayio.FourWire( spi, command=tft_dc, chip_select=tft_cs, reset=board.D6 )
    display = adafruit_ili9341.ILI9341( display_bus, width=320, height=240, rotation=180 )
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

    while True:
        time.sleep(3)

        try:
            color_bitmap = displayio.Bitmap(320, 240, 1)
            color_palette = displayio.Palette(1)
            color_palette[0] = 0x000000
            bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
            splash.append(bg_sprite)


            if cycle_count > 10:
                d.refresh()
                cycle_count = 0

            if (cycle_count % 2) == 0:
                title_text = "Temp"
                body_text = ('Temp: %0.0f°F' % d.getStat('temp'))
                body_text += ('\nHumidity: %d' % d.getStat('humidity'))
                body_text += ('\nBarometric: %d' % d.getStat('barometric_pressure'))

            else:
                title_text = "Air"
                body_text = ("Small dust: %d" % d.getStat('air_quality_small'))
                body_text += ('\nMedium dust: %d' % d.getStat('air_quality_medium'))
                body_text += ('\nBig dust: %d' % d.getStat('air_quality_large'))

            title_text_el = label.Label(font_large, text=title_text, color=0xffffff)
            title_text_el.x = 40
            title_text_el.y = 70
            title_text_el.scale = 1
            splash.append(title_text_el)

            body_text_el = label.Label(font_small, text=body_text, color=0xffffff)
            body_text_el.x = 40
            body_text_el.y = 130
            body_text_el.scale = 1
            splash.append(body_text_el)

            time_text = strftime("%H:%M", time.localtime())
            time_text_el = label.Label(font_small, text=time_text, color=0xaaaaaa)
            time_text_el.x = 15
            time_text_el.y = 15
            time_text_el.scale = 1
            splash.append(time_text_el)

            cycle_count = cycle_count + 1

        except KeyboardInterrupt:
            sys.exit(0)

        except:
            pass
