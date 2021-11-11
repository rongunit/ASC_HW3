# ----------------------------- shape.py ------------------------------
#  Содержит поля и абстрактные методы базового класса "Геометрическая фигура".
# -------------------------------------------------------------------------
from abc import abstractmethod


class Shape:
    def __init__(self, density):
        self.density = density

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def to_string(self):
        pass

    @abstractmethod
    def to_test(self):
        pass
