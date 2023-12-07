# Cálculo de área de un triángulo


def calcular_area_triangulo(coordenada1, coordenada2, coordenada3):
    x1, y1 = coordenada1  # declaramos los puntos x uno, y uno
    x2, y2 = coordenada2  # declaramos los puntos x dos, y dos
    x3, y3 = coordenada3  # declaramos los puntos x tres, y tres

    area = 0.5 * abs(
        (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    )  # Calculamos el area

    return area  # retornamos el  valor area


# Solicimos las coordenadas de los vértices al usuario
def Pedircoord():
    coordenadas = []
    while (
        True
    ):  # iniciamos un bucle para que el usuario siga ingresando coordenadas hasta que indique que no (s/n)
        coordenada = tuple(
            map(
                float,
                input("Ingresa coordenadas del siguiente vértice (x, y): ").split(", "),
            )
        )  # En el objeto coordenada te pedira ingresar los puntos ( , ) ejemplo (1 , 1)
        coordenadas.append(coordenada)  # agrega la coordenada a la lista
        continuar = input("¿Quieres agregar otro vértice? (s/n): ")
        if (
            continuar.lower() != "s"
        ):  # Este if nos indica que si el usuario ingresa diferente a "s" se rompe el bucle
            break
    return coordenadas  # Y aqui retornaria las coordenadas ingresadas por el usuario


vertices = Pedircoord()

# Metodo para calcular el area
if len(vertices) >= 3:  # Verificamos si el usuario al menos a ingresado 3 coordenadas
    if (
        len(vertices) > 3
    ):  # Verifica que si tiene mas de 3 se calculará el area, pero ya no como triangulo
        print(
            "El polígono tiene más de 3 coordenada. Se calculara el area como poligono simple, no como triángulo."
        )  # se imprime el mensaje
    area = (
        0  # Se inicializa una variable llamada area para acumular el área del polígono
    )
    for i in range(
        1, len(vertices) - 1
    ):  # Inicia un bucle for que recorre los vertices desde el segundo hasta el penultimo
        area += calcular_area_triangulo(
            vertices[0], vertices[i], vertices[i + 1]
        )  # Calcula el area de cada triángulo formado por el primer vértice y dos vértices consecutivos

    print(
        f"El area del poligono con vertices {vertices} es: {area}"
    )  # imprime el area del poligono calculado
else:
    print(
        "Se requiere al menos 3 vertices para hallar el area de un poligono."
    )  # Se imprime un mensaje indicando que se necesitan mas de 3 coordenadas para poder hallar un area
