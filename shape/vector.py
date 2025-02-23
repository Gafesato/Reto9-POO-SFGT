import math

from shape.point import Point
from shape.line import Line

class Vector(Line):
    def __init__(self, start_point: "Point", end_point: "Point") -> None:
        super().__init__(start_point, end_point)
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y
        self.vector = Point(self.x, self.y)

    def scalar_product(self, vector2: "Vector") -> float:
        """Devuelve el producto escalar con otro Vector."""
        return (self.x*vector2.x) + (self.y*vector2.y)

    def norm(self) -> float:
        """Retorna la norma del vector."""
        return math.sqrt((self.x)**2 + (self.y)**2)