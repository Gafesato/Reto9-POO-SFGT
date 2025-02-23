from shape.triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._is_right_triangle and not self._check_triangle_type(3):
            raise ValueError("Los vértices dados no forman un triángulo rectángulo.")

    @property
    def _is_right_triangle(self) -> bool:
        """Verifica que el triángulo sea rectángulo usando El Teorema de Pitágoras."""
        c1, c2, hyp = sorted(edge.length**2 for edge in self.edges)
        return round(c1+c2, 7) == round(hyp, 7)