# ----------------------------- tetrahedron.py ------------------------------
#  Содержит все методы для взаимодействия с тетраэдром.
# ---------------------------------------------------------------------------
import math
import random
from shape import Shape


class Tetrahedron(Shape):
    def __init__(self, *args):
        i = len(args[0])
        if i > 2:
            print("Error in Tetrahedron constructor!")
        elif i == 2:
            super().__init__(args[0][0])
            self.edge = args[0][1]
        else:
            print(f"Couldn't parse data \"{args}\", so I generated a random tetrahedron instead")
            self.rnd()

    def volume(self):
        return math.sqrt(2) * (int(self.edge) ** 3) / 12

    #    def read(self, info):#info - string with information about 1 sphere
    #        self.radius = info
    def rnd(self):
        self.edge = random.randint(1, 30)
        self.density = random.randint(1, 30)

    def to_string(self):
        return f"Tetrahedron: Edge = {self.edge}; Density = {self.density}; Volume = {self.volume()}"

    def to_test(self):
        return f"2 {self.density} {self.edge}"


# Вычисляет объем тетраэра
def volume(tetrahedron):
    return math.sqrt(2) * (tetrahedron[1] ** 3) / 12
