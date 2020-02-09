from checks import linear_independently
from vector import Vector


def test_linear_independently():
    assert not linear_independently(Vector(1, 1, 1), Vector(2, 2, 2))
    assert linear_independently(Vector(1, 1, 1), Vector(2, 2, 3))
