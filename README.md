# Reto9-POO-SFGT


## 1. Uso del Decorador `@property` en Shape
Para mejorar el acceso a los datos protegidos en la clase `Shape`, se agregó el decorador `@property`. Este permite acceder a los atributos privados de una manera controlada y segura sin exponer directamente las variables.

Por ejemplo, en lugar de acceder directamente a `self.__method`, se crea un método de acceso:

```python
@property
def get_method(self):
    return self.__method
```

Este enfoque mantiene el encapsulamiento y evita la modificación accidental de los datos internos de la clase.

## 2. Uso de `@classmethod` para Definir y Cambiar el Tipo de Forma
Para permitir la definición y modificación del tipo de figura a nivel de clase, se agregaron los siguientes métodos de clase:

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

Estos métodos permiten establecer y obtener el tipo de figura sin necesidad de instanciar la clase. Esto es útil cuando se requiere que todas las instancias de `Shape` compartan un mismo tipo de figura.

## 3. Uso de un Decorador Personalizado para Medir el Tiempo de Ejecución
Para medir el tiempo de ejecución de ciertos métodos dentro de `Shape`, se utilizó un decorador llamado `@timing_counter`, definido en `shape.decorator`.

Este decorador se aplicó a operaciones como `compute_area` y `compute_perimeter`, así:

```python
@timing_counter
def compute_area(self):
    raise NotImplementedError("Subclases deben implementar compute_area()")

@timing_counter
def compute_perimeter(self) -> float:
    """Retorna la suma de las longitudes de cada arista de la figura."""
    return sum(edge.length for edge in self.edges)
```

El decorador `@timing_counter` mide el tiempo de ejecución de la función y lo imprime en la consola. Esto ayuda a optimizar el rendimiento y a detectar cuellos de botella en los cálculos de área y perímetro.

---

Con estos cambios, la clase `Shape` ahora es más robusta, accesible y eficiente en la gestión de datos y en el monitoreo del rendimiento.

