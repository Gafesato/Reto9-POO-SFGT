from shape.shape_class import Shape
from shape.decorator import timing_counter

class Triangle(Shape):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if len(self.vertices) != 3:
            raise ValueError("Un triángulo debe tener solo 3 vértices.")

    @timing_counter
    def compute_area(self) -> float:
        """Calcula el área con las coordenadas de cada punto del triángulo."""
        x1, x2, x3 = [vertex.x for vertex in self.vertices]
        y1, y2, y3 = [vertex.y for vertex in self.vertices]
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    @property
    def _check_triangle_type(self, unique_sides: int) -> bool:
        sides: list[float] = [edge.length for edge in self.edges]
        # Uso set() ya que solo permite valores únicos
        # En caso de que len(set(...)) == unique_sides,
        # es porque hay unique_sides iguales
        # tomo 7 valores de redondeo para verificar bien
        return len(set(round(side, 7) for side in sides)) == unique_sides