from vector import Vector, Point


class TestVector:
    def get_test_vector(self) -> Vector:
        return Vector(1, 2, 3)

    def get_test_point(self) -> Point:
        return Point(1, 2, 3)

    def test_equality(self):
        v = self.get_test_vector()
        assert v.x1 == 1
        assert v.x2 == 2
        assert v.x3 == 3
        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3
        assert v.coords == [1, 2, 3]
        assert v == self.get_test_vector()
        assert v == self.get_test_point()

    def test_position_vector(self):
        p = self.get_test_point()
        v = p.position_vector
        assert v == self.get_test_vector()
        assert p == self.get_test_point()

    def test_sub(self):
        a = Vector(2, 3, 4)
        b = Vector(1, 1, 1)
        assert a - b == Vector(1, 2, 3)
        assert b - a == Vector(-1, -2, -3)

    def test_add(self):
        a = Vector(1, 2, 3)
        b = Vector(4, 5, 6)
        assert a + b == Vector(5, 7, 9)

    def test_mul(self):
        a = Vector(1, 2, 3)
        assert 2 * a == Vector(2, 4, 6)  # rmul
        assert a * 2 == Vector(2, 4, 6)  # mul
        assert 1.5 * a == Vector(1.5, 3, 4.5)  # rmul
        assert a * 1.5 == Vector(1.5, 3, 4.5)  # mul

    def test_len(self):
        v = Vector(1,0,0)
        assert v.length == 1
        v2 = Vector(0, 1, 0)
        assert v2.length == 1
        v3 = Vector(0, 0, 1)
        assert v3.length == 1
