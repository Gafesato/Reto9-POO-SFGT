from shape.point import Point

class Line:
    """Abstracción de lo que es una línea en el plano."""
    def __init__(self, start_point: "Point", end_point: "Point") -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.start_point.compute_distance(self.end_point)