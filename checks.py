from enum import Enum

from line import Line
from vector import Vector


def linear_independently(g: Vector, h: Vector) -> bool:
    a1 = g.x1 / h.x1 if h.x1 != 0 else 0
    a2 = g.x2 / h.x2 if h.x2 != 0 else 0
    a3 = g.x3 / h.x3 if h.x3 != 0 else 0
    return not a1 == a2 == a3


def is_vector_on_line(v: Vector, l: Line) -> bool:
    r = []

    for i in range(3):
        r.append((v[i] - l.sv[i]) / l.dv[i])

    return r[0] == r[1] == r[2]


def have_intersection(g: Line, h: Line) -> bool:
    x1, x2, x3 = g.support_vector.coords
    y1, y2, y3 = g.direction_vector.coords
    a1, a2, a3 = h.support_vector.coords
    b1, b2, b3 = h.direction_vector.coords

    if b1 == 0:
        s = -((x1 - a1) / y1)

        t1 = (x2 - a2 + s * y2) / b2
        t2 = (x3 - a3 + s * y3) / b3

        return t1 == t2

    else:

        p1_1 = x2 - a2 - ((x1 * b2) / b1) + ((a1 * b2) / b1)
        p1_2 = ((y1 * b2) / b1) - y2
        s1 = p1_1 / p1_2

        p2_1 = x3 - a3 - ((x1 * b3) / b1) + ((a1 * b3) / b1)
        p2_2 = ((y1 * b3) / b1) - y3
        s2 = p2_1 / p2_2

        return s1 == s2


class LineRelationType(Enum):
    IDENTICAL = 0
    PARALLEL = 1
    INTERSECTION = 2
    SKEW = 3


def get_line_relation_type(g: Line, h: Line) -> LineRelationType:
    if not linear_independently(g.dv, h.dv):
        # Linear dependently: Identical or parallel
        if is_vector_on_line(g.sv, h):
            return LineRelationType.IDENTICAL
        else:
            return LineRelationType.PARALLEL
    else:
        # Linear independently: Intersection or skew
        if have_intersection(g, h):
            return LineRelationType.INTERSECTION
        else:
            return LineRelationType.SKEW