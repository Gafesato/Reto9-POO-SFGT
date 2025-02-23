from shape.triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._check_triangle_type(1):
            raise ValueError("Los vértices dados no forman un triángulo equilátero.")