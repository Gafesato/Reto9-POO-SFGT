class Point:
    """Abstracción de lo que es un punto en el plano."""
    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point") -> float:
        """Calcula la distancia entre dos puntos."""
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5