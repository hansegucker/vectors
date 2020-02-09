from math import sqrt
from typing import Union


class ObjectOf3:
    def __init__(self, x1, x2, x3):
        self.coords = [x1, x2, x3]

    @property
    def x1(self) -> float:
        return self.coords[0]

    @x1.setter
    def x1(self, x: float):
        self.coords[0] = x

    @property
    def x2(self) -> float:
        return self.coords[1]

    @x2.setter
    def x2(self, x: float):
        self.coords[1] = x

    @property
    def x3(self) -> float:
        return self.coords[2]

    @x3.setter
    def x3(self, x: float):
        self.coords[2] = x

    def __getitem__(self, key: int) -> float:
        return self.coords[key]

    def __setitem__(self, key: int, value: float):
        self.coords[key] = value

    def __eq__(self, other) -> bool:
        return self.coords == other.coords


class Point(ObjectOf3):
    def __str__(self) -> str:
        return "({}|{}|{})".format(self.x1, self.x2, self.x3)

    @property
    def position_vector(self):
        return Vector(self.x1, self.x2, self.x3)


class Vector(ObjectOf3):
    def __str__(self) -> str:
        return "/{}\\\n|{}|\n\\{}/".format(self.x1, self.x2, self.x3)

    @property
    def point(self):
        return Point(self.x1, self.x2, self.x3)

    def __sub__(self, other):
        return Vector(self.x1 - other.x1, self.x2 - other.x2, self.x3 - other.x3)

    def __add__(self, other):
        return Vector(self.x1 + other.x1, self.x2 + other.x2, self.x3 + other.x3)

    def __mul__(self, r: Union[float, int]):
        return Vector(self.x1 * r, self.x2 * r, self.x3 * r)

    def __rmul__(self, r: Union[float, int]):
        return self.__mul__(r)

    @property
    def length(self):
        return sqrt(self.x1 ** 2 + self.x2 ** 2 + self.x3 ** 2)
