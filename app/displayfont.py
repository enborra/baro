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
    height=240
)

splash = displayio.Group()
display.show(splash)


font_file = "app/futura-medium-72.ttc"

font = bitmap_font.load_font(font_file)

bitmap = displayio.Bitmap(display.width, display.height, 2)

palette = displayio.Palette(2)

palette[0] = 0x000000
palette[1] = 0xFFFFFF

_, height, _, dy = font.get_bounding_box()
for y in range(height):
    pixels = []
    for c in "Adafruit CircuitPython":
        glyph = font.get_glyph(ord(c))
        if not glyph:
            continue
        glyph_y = y + (glyph.height - (height + dy)) + glyph.dy

        if 0 <= glyph_y < glyph.height:
            for i in range(glyph.width):
                value = glyph.bitmap[i, glyph_y]
                pixel = 0
                if value > 0:
                    pixel = 1
                pixels.append(pixel)
        else:
            # empty section for this glyph
            for i in range(glyph.width):
                pixels.append(0)

        # one space between glyph
        pixels.append(0)

    if pixels:
        for x, pixel in enumerate(pixels):
            bitmap[x, y] = pixel

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group to hold the TileGrid
group = displayio.Group()

group.x = 20
# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

while True:
    pass
