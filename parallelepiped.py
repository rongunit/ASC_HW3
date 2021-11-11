# ----------------------------- parallelepiped.py ------------------------------
#  Содержит все методы для взаимодействия с параллелепипедом.
# -------------------------------------------------------------------------
import random
from shape import Shape


class Parallelepiped(Shape):
    def __init__(self, *args):
        i = len(args[0])
        if i > 4:
            print("Error in Parallelepiped constructor!")
        elif i == 4:
            super().__init__(args[0][0])
            self.a = args[0][1]
            self.b = args[0][2]
            self.c = args[0][3]
        else:
            print(f"Couldn't parse data \"{args}\", so I generated a random parallelepiped instead")
            self.rnd()

    def volume(self):
        return int(self.a) * int(self.b) * int(self.c)

    def rnd(self):
        self.a = random.randint(1, 30)
        self.b = random.randint(1, 30)
        self.c = random.randint(1, 30)
        self.density = random.randint(1, 30)

    def to_string(self):
        return f"Parallelepiped: Density = {self.density}; a = {self.a}; b = {self.b}; c = {self.c}; Volume = {self.volume()}"

    def to_test(self):
        return f"3 {self.density} {self.a} {self.b} {self.c}"


# Вычисляет объем параллелепипеда
def volume(parallelepiped):
    return float(parallelepiped[1] * parallelepiped[2] * parallelepiped[3])
