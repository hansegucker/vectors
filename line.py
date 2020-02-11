from vector import Vector


class Line:
    def __init__(self, support_vector: Vector, direction_vector: Vector):
        self.support_vector = support_vector
        self.direction_vector = direction_vector

    @property
    def sv(self):
        return self.support_vector

    @property
    def dv(self):
        return self.direction_vector

    def __str__(self):
        return "{} + r · {}".format(self.support_vector, self.direction_vector)