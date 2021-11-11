# ----------------------------- sphere.py ------------------------------
#  Содержит все методы для взаимодействия со сферой.
# -----------------------------------------------------------------------
import math
import random
from shape import Shape


class Sphere(Shape):
    def __init__(self, *args):
        i = len(args[0])
        if i > 2:
            print("Error in Sphere constructor!")
        elif i == 2:
            super().__init__(args[0][0])
            self.radius = args[0][1]
        else:
            print(f"Couldn't parse data\"{args}\", so I generated a random sphere instead")
            self.rnd()

    def volume(self):
        return float(4 / 3 * math.pi * (int(self.radius) ** 3))

#    def read(self, info):#info - string with information about 1 sphere
#        self.radius = info
    def rnd(self):
        # добавляет радиус фигуры
        self.radius = random.randint(1, 30)
        self.density = random.randint(1, 30)

    def to_string(self):
        return f"Sphere: r = {self.radius}; Density = {self.density}; Volume = {self.volume()}"

    def to_test(self):
        return f"1 {self.density} {self.radius}"

