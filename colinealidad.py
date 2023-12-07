# Calculo de colinealidad de tres puntos en el plano.


def areaTriangulo(coordenada1, coordenada2, coordenada3):
    x1, y1 = coordenada1  # declaramos los puntos x uno, y uno
    x2, y2 = coordenada2  # declaramos los puntos x dos, y dos
    x3, y3 = coordenada3  # declaramos los puntos x dos, y dos

    area = 0.5 * abs(
        (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    )  # Calculamos el area

    return area  # retornamos el  valor area


def PuntosColineales(coordenada1, coordenada2, coordenada3):
    # Calcular el área del triángulo formado por los tres puntos
    area_triangulo = areaTriangulo(coordenada1, coordenada2, coordenada3)
    # Si el área es muy cercana a cero, los puntos son colineales
    return area_triangulo == 0


def PedirCoord():
    coordenadas = []
    for _ in range(
        3
    ):  # Cuando no sequiere crear una variable se ingresa "_" de rango 3
        coordenada = tuple(
            map(float, input("Ingresa coordenadas del vértice (x, y): ").split(", "))
        )  # Se solicita la entrada de coordenadas al usuario y aca lo divide en separadores con un "," ejemplo 1, 1
        coordenadas.append(coordenada)  # agrega la coordenada a la lista
    return coordenadas  # Aqui retornaria las coordenadas ingresadas por el usuario


vertices = PedirCoord()  # Solicita las coordenadas de los vertices

if len(vertices) == 3:  # verifica si la longitud ( len) es igual a 3
    if PuntosColineales(vertices[0], vertices[1], vertices[2]):
        print(
            "Los puntos ingresados son colineales."
        )  # se imprime los puntos ingresados son colineales
    else:
        print(
            "Los puntos ingresados no son colineales."
        )  # se imprime los puntos ingresados no son colineales
        area = sum(
            areaTriangulo(vertices[i], vertices[i + 1], vertices[i + 2])
            for i in range(
                len(vertices) - 2
            )  # Te permite calcular el area del poligono formado por los vertices
        )
        print(
            f"El area del poligono con vertices {vertices} es: {area}"
        )  # se imprime el area del poligono
else:
    print(
        "Se requiere las 3 coordenadas para hallar la colinealidad y calcular el area."  # Este else nos indica que se requiere las 3 coordenadas de los vertices para hallar la colinealidad y calcular el area
    )
