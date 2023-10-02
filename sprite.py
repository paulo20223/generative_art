import random
from time import sleep

from PIL import Image, ImageDraw


class SpriteGenerator:

    def __init__(self):
        self.list_sym = []

    @staticmethod
    def random_color(count=1):
        if count > 1:
            return [tuple(random.choices(range(50, 215), k=3)) for _ in range(count)]
        return random.choices(range(50, 215), k=3)

    def create_square(self, border, draw, rand_color, element, size):
        if element == int(size / 2):
            draw.rectangle(border, rand_color)
        elif len(self.list_sym) == element + 1:
            draw.rectangle(border, self.list_sym.pop())
        else:
            self.list_sym.append(rand_color)
            draw.rectangle(border, rand_color)

    def create_invader(self, border, draw, size):
        x0, y0, x1, y1 = border
        square_size = (x1 - x0) / size
        rand_colors = self.random_color(3)
        rand_colors += [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        i = 1
        for y in range(0, size):
            i *= -1
            element = 0
            for x in range(0, size):
                top_left_x = x * square_size + x0
                top_left_y = y * square_size + y0
                bot_right_x = top_left_x + square_size
                bot_right_y = top_left_y + square_size
                self.create_square((top_left_x, top_left_y, bot_right_x, bot_right_y),
                                   draw, random.choice(rand_colors), element, size)

                if element == int(size / 2) or element == 0:
                    i *= -1
                    element += i

    def main(self, size=4, invaders=1, img_size=1000):
        image = Image.new('RGB', (img_size, img_size))
        draw = ImageDraw.Draw(image)
        invader_size = img_size / invaders
        padding = invader_size / (size + 2)
        for x in range(0, invaders):
            for y in range(0, invaders):
                top_left_x = x * invader_size + padding
                top_left_y = y * invader_size + padding
                bot_right_x = invader_size - padding
                bot_right_y = invader_size - padding
                self.create_invader((top_left_x, top_left_y, bot_right_x, bot_right_y), draw, size)
        image.save("stripe.jpg", format="JPEG")


if __name__ == '__main__':
    # SpriteGenerator().main(random.randint(10, 20), 1)
    SpriteGenerator().main(3, 1)
