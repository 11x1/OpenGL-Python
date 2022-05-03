import random

class Pixels:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [255 for i in range(width * height * 3)]
    
    def set_pixel(self, x, y, r, g, b):
        self.pixels[(y * self.width + x) * 3] = r
        self.pixels[(y * self.width + x) * 3 + 1] = g
        self.pixels[(y * self.width + x) * 3 + 2] = b
    
    def get_pixel(self, x, y):
        return self.pixels[(y * self.width + x) * 3], self.pixels[(y * self.width + x) * 3 + 1], self.pixels[(y * self.width + x) * 3 + 2]

    def get_pixels(self):
        return self.pixels

    def randomize(self):
        for i in range(len(self.pixels)):
            self.pixels[i] = random.randint(0, 255)
