from checks import (
    linear_independently,
    is_vector_on_line,
    get_line_relation_type,
    LineRelationType,
)
from line import Line
from vector import Vector


def test_linear_independently():
    assert not linear_independently(Vector(1, 1, 1), Vector(2, 2, 2))
    assert linear_independently(Vector(1, 1, 1), Vector(2, 2, 3))


class TestLineRelation:
    @staticmethod
    def get_test_lines_identical():
        g = Line(Vector(2, 0, 2), Vector(1, 2, 1))
        h = Line(Vector(4, 4, 4), Vector(-1, -2, -1))
        return g, h

    @staticmethod
    def get_test_lines_parallel():
        g = Line(Vector(3, 0, 3), Vector(1, 2, 1))
        h = Line(Vector(4, 4, 4), Vector(-1, -2, -1))
        return g, h

    def test_linear_independently(self):
        g, h = self.get_test_lines_identical()
        assert not linear_independently(g.dv, h.dv)
        g, h = self.get_test_lines_parallel()
        assert not linear_independently(g.dv, h.dv)

    def test_is_vector_on_line_true(self):
        g, h = self.get_test_lines_identical()
        assert is_vector_on_line(g.sv, h)
        assert is_vector_on_line(h.sv, g)

    def test_is_vector_on_line_false(self):
        g, h = self.get_test_lines_parallel()
        assert not is_vector_on_line(g.sv, h)
        assert not is_vector_on_line(h.sv, g)

    def test_relation_identical(self):
        g, h = self.get_test_lines_identical()
        assert get_line_relation_type(g, h) == LineRelationType.IDENTICAL

    def test_relation_parallel(self):
        g, h = self.get_test_lines_parallel()
        assert get_line_relation_type(g, h) == LineRelationType.PARALLEL
