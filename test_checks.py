from checks import (
    linear_independently,
    is_vector_on_line,
    get_line_relation_type,
    LineRelationType,
    have_intersection)
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

    @staticmethod
    def get_test_lines_intersection():
        g = Line(Vector(1, 1, 1), Vector(1, 0, 2))
        h = Line(Vector(2, 1, 3), Vector(4, 1, 3))
        return g, h

    @staticmethod
    def get_test_lines_skew():
        g = Line(Vector(-2, 3, 2), Vector(3, -1.5, 1))
        h = Line(Vector(1, -6, 5), Vector(15, 0, 2))
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
        assert get_line_relation_type(h, g) == LineRelationType.IDENTICAL

    def test_relation_parallel(self):
        g, h = self.get_test_lines_parallel()
        assert get_line_relation_type(g, h) == LineRelationType.PARALLEL
        assert get_line_relation_type(h, g) == LineRelationType.PARALLEL

    def test_have_intersection_true(self):
        g, h = self.get_test_lines_intersection()
        assert have_intersection(g, h)
        assert have_intersection(h, g)

    def test_have_intersection_false(self):
        g, h = self.get_test_lines_skew()
        assert not have_intersection(g, h)
        assert not have_intersection(h, g)

    def test_line_relation_intersection(self):
        g, h = self.get_test_lines_intersection()
        assert get_line_relation_type(g, h) == LineRelationType.INTERSECTION
        assert get_line_relation_type(h, g) == LineRelationType.INTERSECTION

    def test_line_relation_skew(self):
        g,h = self.get_test_lines_skew()
        assert get_line_relation_type(g, h) == LineRelationType.SKEW
        assert get_line_relation_type(h, g) == LineRelationType.SKEW
