from checks import is_vector_on_line, have_intersection
from line import Line
from vector import Vector

g = Line(Vector(1, 1, 1), Vector(1, 0, 2))
h = Line(Vector(2,1,3), Vector(4, 1, 3))

print(g, h)

print(have_intersection(g, h))