import math
import random

try:
    from shape.exceptions import ValorInvalidoArgs
    from shape.line import Line
    from shape.point import Point
    from shape.vector import Vector
    # Esto genera un error si se __name__ == '__main__',
    # ya que este archivo funciona como módulo y no como
    # un ejecutable en sí.
except (ImportError, ModuleNotFoundError):
    print("Error al importar la librería desde el módulo actual. ¡Ejecute desde main.py!")

from shape.decorator import timing_counter

class Shape:
    _shape_type = None # Atributo de Clase
    def __init__(self, method: int, *args) -> None:
        """Inicializar Shape con vértices o aristas."""
        self.vertices: list["Point"] = []
        self.edges: list["Line"] = []
        self.__method: int = method

        if len(args) <= 2:
            raise ValorInvalidoArgs("No se han proporcionado el número adecuado de vértices o aristas para la Figura.")

        if not all(isinstance(arg, (Point, Line)) for arg in args):
            raise ValorInvalidoArgs("Todos los argumentos deben ser instancias de Point o Line.")

        # Inicialización con vértices
        if method == 1:
            for i in range(len(args)):
                vertice: "Point" = args[i]
                self.vertices.append(vertice)
                edge: "Line" = Line(vertice, args[(i + 1) % len(args)])
                self.edges.append(edge)

        # Inicialización con aristas
        elif method == 2:
            for edge in args:
                self.edges.append(edge)
                if edge.start_point not in self.vertices:
                    self.vertices.append(edge.start_point)
                if edge.end_point not in self.vertices:
                    self.vertices.append(edge.end_point)

        else:
            raise ValueError("No se seleccionó ningún método válido al inicializar.")

        # Verificar que es una Figura bien definida
        flag, issue = self._check_is_valid_shape
        if not flag:
            raise ValorInvalidoArgs(f"La Figura no es correcta: {issue}")

    @property
    def get_method(self):
        return self.__method

    def set_method(self, new_method):
        self.__method == new_method

    @timing_counter
    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    @timing_counter
    def compute_perimeter(self) -> float:
        """Retorna la suma de las longitudes de cada arista de la figura."""
        return sum(edge.length for edge in self.edges)
    
    @timing_counter
    def compute_inner_angles(self) -> list[float]:
        """Calcula los ángulos en cada vértice."""
        angles = []
        n = len(self.vertices)
        for i in range(n):
            p1 = self.vertices[i - 1]
            p2 = self.vertices[i]
            p3 = self.vertices[(i + 1) % n]

            # Creo la clase Vector para facilitar el cálculo
            # de los ángulos
            v1 = Vector(p2, p1)
            v2 = Vector(p2, p3)
            angle = 0 # Este es por si lanza excepción y no se cuelgue el programa
            try:
                cos_theta = v1.scalar_product(v2) / (v1.norm() * v2.norm())
                angle = math.degrees(math.acos(cos_theta))
            except (ZeroDivisionError, ValueError) as error:
                print(f"Se ha generado un error -> {error}")
            finally:
                angles.append(angle)
        return angles
    
    @property
    def _check_is_valid_shape(self) -> bool:
        """Verifica si la figura es válida (es una figura cerrada y no colineal)."""
        if len(self.edges) != len(self.vertices):  
            return [False, "El número de aristas y vértices no es el mismo."]  # Debe haber el mismo número de aristas y vértices

        # Verificar si al menos 3 puntos consecutivos son colineales
        for i in range(len(self.vertices)):
            p1 = self.vertices[i - 2]
            p2 = self.vertices[i - 1]
            p3 = self.vertices[i]

            # Determinante para verificar colinealidad
            det = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
            if det == 0:
                return [False, "Hay puntos colineales que no forman una figura."]  # Si el determinante es 0, los puntos son colineales

        # Crear un conjunto de conexiones para verificar si cada vértice está bien conectado
        connections = {vertex: [] for vertex in self.vertices}
        
        for edge in self.edges:
            connections[edge.start_point].append(edge.end_point)
            connections[edge.end_point].append(edge.start_point)

        # Empezar desde un vértice y recorrer toda la figura para verificar que es un ciclo
        visited = set()
        stack = [self.vertices[0]]  # Iniciar desde cualquier punto

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(connections[current])  # Agregar los puntos conectados

        return [True, len(visited)]
    
    @classmethod
    def set_shape_type(cls, shape_type: str):
        """Permite definir o cambiar el tipo de la figura."""
        cls._shape_type = shape_type

    @classmethod
    def get_shape_type(cls):
        """Retorna el tipo de figura definido a nivel de clase."""
        return cls._shape_type

    def __str__(self) -> str:
        """Mostrar una representación agradable de la figura en cuestión."""
        output = "Vértices: "
        for vertice in self.vertices:
            output += f'[({vertice.x},{vertice.y})] '
        output += "\nAristas: "
        for edge in self.edges:
            output += f'[({edge.start_point.x}),({edge.start_point.y})] -> [({edge.end_point.x}),({edge.end_point.y})]]  '
        return output


if __name__ == '__main':
    figurita = Shape(1)