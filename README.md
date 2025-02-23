 # Reto9-POO-SFGT

## 1. Uso del Decorador `@property` en Shape
En la clase `Shape`, agrego el decorador `@property` a los métodos protegidos.
Por ejemplo, en lugar de acceder directamente a `self.__method`, creo el getter:

```python
@property
def get_method(self):
    return self.__method
```
```python
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
```
Así se puede ver que a la hora de llamar una de estas funciones decoradas, se hace como si fuese un atributo. Veamos por ejemplo:
```python
# Verificar que es una Figura bien definida
flag, issue = self._check_is_valid_shape
if not flag:
    raise ValorInvalidoArgs(f"La Figura no es correcta: {issue}")
```
---
## 2. Uso de `@classmethod`
Esto permite cambiar y definir el tipo de forma que le corresponde a Shape, esto se puede hacer sin instanciar, sino accediendo al atributo de clase _shape_type.
```python
class Shape:
    _shape_type = None  # Atributo de clase

    @classmethod
    def set_shape_type(cls, shape_type: str):
        """Permite definir o cambiar el tipo de la figura."""
        cls._shape_type = shape_type

    @classmethod
    def get_shape_type(cls):
        """Retorna el tipo de figura definido a nivel de clase."""
        return cls._shape_type
```

## 3. Uso de un Decorador Personalizado
Para medir el tiempo de ejecución de ciertos métodos dentro de `Shape`, uso un decorador llamado `@timing_counter`, definido en `shape.decorator`, así ayudo con el trabajo de módulos y paquetes para que el código siga siendo escalable.
Este decorador se lo apliqué a operaciones como `compute_area` y `compute_perimeter`, así:

```python
@timing_counter
def compute_area(self):
    raise NotImplementedError("Subclases deben implementar compute_area()")

@timing_counter
def compute_perimeter(self) -> float:
    """Retorna la suma de las longitudes de cada arista de la figura."""
    return sum(edge.length for edge in self.edges)
```
Además se lo agregué a otras clases que heredan de `Shape` como `Triangle`
```python
@timing_counter
def compute_area(self) -> float:
    """Calcula el área con las coordenadas de cada punto del triángulo."""
    x1, x2, x3 = [vertex.x for vertex in self.vertices]
    y1, y2, y3 = [vertex.y for vertex in self.vertices]
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
```

El decorador `@timing_counter` mide el tiempo que le toma a la función que se está decorando ejecutarse, uso `__name__` para saber que función se trabaja en cuestión dentro de `wrapper()` que actúa como la función interna del decorador.
```python
import time

def timing_counter(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(2)
        result = function(*args, **kwargs)
        end = time.time()
        print(f"A la función {function.__name__} le tomó {end-start:.5f} segundos realizar su proceso.")
        return result
    return wrapper
```
También, para probar el uso múltiple de los decoradores, apliqué @property y luego @timing_counter a compute_area(), método de la clase Rectangle
```python
@property
@timing_counter
def compute_area(self) -> float:
    return self._width * self._height
```
Lo cual, la llamada en main.py corresponde a `rectangle.compute_area`, como si fuese un atributo.
```python
print(f"Área del rectángulo: {rectangle.compute_area}")
```
---

## Salida
Con los cambios implementados, veamos ahora como es la salida por consola del mismo código que se usó en el reto 6.
```bash
--------------------
Rectángulo
--------------------
Esta llamada corresponde a la verificación interna de Rectangle()
A la función compute_inner_angles le tomó 2.00111 segundos realizar su proceso.
------------
A la función compute_area le tomó 2.00191 segundos realizar su proceso.
Área del rectángulo: 50
A la función compute_perimeter le tomó 2.00148 segundos realizar su proceso.
Perímetro del rectángulo: 30.0
A la función compute_inner_angles le tomó 2.00169 segundos realizar su proceso.
Ángulos internos del rectángulo: [90.0, 90.0, 90.0, 90.0]
--------------------
Triángulo
--------------------
A la función compute_area le tomó 2.00178 segundos realizar su proceso.
Área del triángulo rectángulo: 25.0
A la función compute_inner_angles le tomó 2.00162 segundos realizar su proceso.
Ángulos internos del triángulo rectángulo: [90.0, 26.565051177077994, 63.43494882292201]
```

