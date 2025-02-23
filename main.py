from shape.point import Point
from shape.rectangle import Rectangle
from shape.trirectangle import TriRectangle
from shape.shape_class import Shape

from shape.exceptions import ValorInvalidoArgs

def main():
    p1 = Point(0, 0)
    p2 = Point(10, 0)
    p3 = Point(10, 5)
    p4 = Point(0, 5)

    print("-"*20)
    print("Rectángulo")
    print("-"*20)
    rectangle = Rectangle(1, p1, p2, p3, p4)
    print("------------")
    print(f"Área del rectángulo: {rectangle.compute_area()}")
    print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")
    print(f"Ángulos internos del rectángulo: {rectangle.compute_inner_angles()}")
    
    print("-"*20)
    print("Triángulo")
    print("-"*20)
    trirectangle = TriRectangle(1, p1, p2, p4)
    print(f"Área del triángulo rectángulo: {trirectangle.compute_area()}")
    print(f"Ángulos internos del triángulo rectángulo: {trirectangle.compute_inner_angles()}")


    # Código Reto 9

def main2():
    try:
        # ERROR 1
        # Este levanta ValueError diciendo que no se
        # selecciono método válido al inicializar
        #shape = Shape(0)

        # ERROR 2
        # Como toda figura debe tener 3 vértices o más
        # Al instanciar Shape solo con 2 puntos, va a levantar
        # el error personalizado.
        # Funciona igual al instanciar solo con 2 aristas
        shape = Shape(1, Point(), Point(2,2), Point(4,4), Point(5,5), Point(6,6))

        # ERROR 3
        # Se genera cuando se llama al método compute_area()
        # directamente desde el objeto shape. Esto debe alzar
        # un error porque no se sabe qué polígono es
        #print(shape.compute_area())
        print(shape.compute_perimeter())

    except ValorInvalidoArgs as e:
        print(f"Error de argumentos-> {e}")
    except NotImplementedError as e:
        print(f"Error de implementación-> {e}")
    except Exception as e:
        print(f"Error inesperado-> {e}")

if __name__ == '__main__':
    main()