from io import BytesIO

import cairo
import random

from lib.palettes import hex_to_tuple, PALETTES
from lib.colors import shades


def pyramid(ctx, x, y, width, height, color, random_center=True):
    if random_center:
        center = (random.randint(x + 3, x + width - 3), random.randint(y + 3, y + height - 3))
    else:
        center = (x + width // 2, y + height // 2)
    tl = (x, y)
    tr = (x + width, y)
    bl = (x, y + height)
    br = (x + width, y + height)
    cols = shades(color, 5)
    triangle(ctx, tl, tr, center, cols[0])
    triangle(ctx, tr, br, center, cols[1])
    triangle(ctx, br, bl, center, cols[2])
    triangle(ctx, bl, tl, center, cols[3])


def triangle(ctx, p1, p2, p3, color):
    ctx.move_to(*p1)
    for p in [p1, p2, p3]:
        ctx.line_to(*p)
    ctx.set_source_rgb(*color)
    ctx.fill()


def main(size=1000, palette=random.choice(PALETTES), pyramid_size=3):
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ims.set_fallback_resolution(300.0, 300.0)
    ctx = cairo.Context(ims)

    # Background
    ctx.rectangle(0, 0, size, size)
    ctx.set_source_rgb(*hex_to_tuple(palette['background']))
    ctx.fill()
    img = BytesIO()
    for x in range(0, size, size // pyramid_size):
        for y in range(0, size, size // pyramid_size):
            pyramid(ctx, x, y, size // pyramid_size, size // pyramid_size,
                    hex_to_tuple(random.choice(palette['colors'])))
    ims.write_to_png("output-piramid.jpg")
    return img


if __name__ == "__main__":
    for idx in range(5):
        item = main(500, random.choice(PALETTES), random.randint(6, 15))
        print(item)
