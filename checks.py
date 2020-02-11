from enum import Enum

from line import Line
from vector import Vector


def linear_independently(g: Vector, h: Vector) -> bool:
    a1 = g.x1 / h.x1
    a2 = g.x2 / h.x2
    a3 = g.x3 / h.x3
    return not a1 == a2 == a3


def is_vector_on_line(v: Vector, l: Line) -> bool:
    r = []

    for i in range(3):
        r.append((v[i] - l.sv[i]) / l.dv[i])

    return r[0] == r[1] == r[2]


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
        return LineRelationType.INTERSECTION
