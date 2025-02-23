from shape.triangle import Triangle

class Isosceles(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._check_triangle_type(2):
            raise ValueError("Los vértices dados no forman un triángulo isósceles.")