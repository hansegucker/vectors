from checks import is_vector_on_line
from line import Line
from vector import Vector

g = Line(Vector(2, 0, 2), Vector(1, 2, 1))
h = Line(Vector(4, 4, 4), Vector(-1, -2, -1))

print(g, h)

print(is_vector_on_line(g.sv, h))