from shape.shape_class import Shape
from shape.decorator import timing_counter

class Rectangle(Shape):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if len(self.vertices) != 4:
            raise ValueError("Un rectángulo debe tener 4 vértices.")
        if not self._check_is_rectangle:
            raise ValueError("Los vértices dados no forman un rectángulo.")

        x_coords = [vertex.x for vertex in self.vertices]
        y_coords = [vertex.y for vertex in self.vertices]

        self._width = max(x_coords) - min(x_coords)
        self._height = max(y_coords) - min(y_coords)

    #@property
    def get_width(self):
        return self._width

    #@property
    def get_height(self):
        return self._height

    @property
    def _check_is_rectangle(self) -> bool:
        """Verifica si los vértices forman un rectángulo verificando ángulos internos."""
        print("Esta llamada corresponde a la verificación interna de Rectangle()")
        angles = self.compute_inner_angles()
        return all(int(angle) == 90 for angle in angles)

    @timing_counter
    def compute_area(self) -> float:
        return self._width * self._height