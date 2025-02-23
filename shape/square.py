from shape.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if self._width != self._height:
            raise ValueError("Los vértices dados no forman un cuadrado.")

    def compute_area(self) -> float:
        return self._width**2