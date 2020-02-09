from vector import Vector


def linear_independently(g: Vector, h: Vector) -> bool:
    a1 = g.x1 / h.x1
    a2 = g.x2 / h.x2
    a3 = g.x3 / h.x3
    return not a1 == a2 == a3
