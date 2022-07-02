import signal
import sys
import time
from time import strftime
from datetime import date
import calendar

# import board
# import displayio
# import adafruit_ili9341
# from adafruit_rgb_display import color565
# from adafruit_display_text import label
# from adafruit_bitmap_font import bitmap_font

from models.Detector import Detector
from models.Thing import HeadsUpDisplay


def keyboardHandler(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, keyboardHandler)

if __name__ == "__main__":
    d = Detector()
    d.refresh()

    # hud = Thing()
    # hud.show()

    # displayio.release_displays()
    #
    # spi = board.SPI()
    # tft_cs = board.CE0
    # tft_dc = board.D25
    #
    # display_bus = displayio.FourWire( spi, command=tft_dc, chip_select=tft_cs, reset=board.D6 )
    # display = adafruit_ili9341.ILI9341( display_bus, width=320, height=240, rotation=180 )
    # splash = displayio.Group()
    #
    # # Blank the screen
    #
    # color_bitmap = displayio.Bitmap(320, 240, 1)
    # color_palette = displayio.Palette(1)
    # color_palette[0] = 0x000000
    # bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
    # splash.append(bg_sprite)
    #
    # display.show(splash)

    # font_large = bitmap_font.load_font("fonts/futura-medium-35.bdf")
    # font_small = bitmap_font.load_font("fonts/futura-medium-20.bdf")
    cycle_count = 0
    displayFace = 0

    # # Create the ui components
    #
    # txtTitle = label.Label( font_large, text='', color=0xffffff, x=40, y=70, scale=1 )
    # splash.append( txtTitle )
    #
    # txtBody = label.Label( font_small, text='', color=0xffffff, x=40, y=130, scale=1 )
    # splash.append( txtBody )
    #
    # txtTime = label.Label( font_small, text='', color=0xaaaaaa, x=15, y=15, scale=1 )
    # splash.append( txtTime )

    while True:
        time.sleep(3)

        try:
            if cycle_count > 10:
                d.refresh()
                cycle_count = 0

            if( displayFace == 0 ):
                title_text = "Temp"
                body_text = ('Temp: %0.0f°F' % d.getStat('temp'))
                body_text += ('\nHumidity: %d' % d.getStat('humidity'))
                body_text += ('\nBarometric: %d' % d.getStat('barometric_pressure'))
                displayFace = 1

            elif( displayFace == 1 ):
                title_text = "Air"
                body_text = ("Small dust: %d" % d.getStat('air_quality_small'))
                body_text += ('\nMedium dust: %d' % d.getStat('air_quality_medium'))
                body_text += ('\nBig dust: %d' % d.getStat('air_quality_large'))
                displayFace = 0

            else:
                displayFace = 0

            # hud.setText( title=title_text, body=body_text )

            # txtTime.text = strftime("%H:%M", time.localtime())
            # txtTitle.text = title_text
            # txtBody.text = body_text

            cycle_count = cycle_count + 1

        except Exception as e:
            print(e)

        sys.stdout.flush()
