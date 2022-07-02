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


class HeadsUpDisplay():
    _spi = None
    _tft_cs = None
    _tft_dc = None
    _tft_reset = None
    _displayBus = None
    _displayWidth = 320
    _displayHeight = 240
    _displayRotation = 180
    _display = None
    _splash = None
    _bg_sprite = None
    _fontLarge = None
    _fontSmall = None
    _txtTime = None
    _txtTitle = None
    _txtBody = None


    def __init__(self, *args, **kwargs):
        pass
    #     self._tft_cs = board.CE0
    #     self._tft_dc = board.D25
    #     self._tft_reset = board.D6
    #
    #     displayio.release_displays()
    #
    #     self._displayBus = displayio.FourWire( self._spi, command=self._tft_dc, chip_select=self._tft_cs, reset=self._tft_reset )
    #     self._display = adafruit_ili9341.ILI9341( self._display_bus, width=self._displayWidth, height=self._displayHeight, rotation=self._displayRotation )
    #     self._splash = displayio.Group()
    #
    #     # Blank the screen
    #
    #     color_bitmap = displayio.Bitmap(320, 240, 1)
    #     color_palette = displayio.Palette(1)
    #     color_palette[0] = 0x000000
    #
    #     self._bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
    #     self._splash.append(bg_sprite)
    #     self._display.show(splash)
    #
    #     _fontLarge = bitmap_font.load_font("fonts/futura-medium-35.bdf")
    #     _fontSmall = bitmap_font.load_font("fonts/futura-medium-20.bdf")
    #
    #     # Create the ui components
    #
    #     self._txtTitle = label.Label( font_large, text='', color=0xffffff, x=40, y=70, scale=1 )
    #     splash.append( self._txtTitle )
    #
    #     self._txtBody = label.Label( font_small, text='', color=0xffffff, x=40, y=130, scale=1 )
    #     splash.append( self._txtBody )
    #
    #     self._txtTime = label.Label( font_small, text='', color=0xaaaaaa, x=15, y=15, scale=1 )
    #     splash.append( self._txtTime )
    #
    # def setText(self, *args, **kwargs):
    #     title_text = kwargs.get('title')
    #     body_text = kwargs.get('body')
    #
    #     self._txtTime.text = strftime("%H:%M", time.localtime())
    #     self._txtTitle.text = title_text
    #     self._txtBody.text = body_text
