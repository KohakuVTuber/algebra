# Cálculo de volumen de un tetraedro


def calcular_volumen_tetraedro(coordenada1, coordenada2, coordenada3, coordenada4):
    x1, y1, z1 = coordenada1  # declaramos los puntos: x uno, y uno, z uno
    x2, y2, z2 = coordenada2  # declaramos los puntos: x dos, y dos, z dos
    x3, y3, z3 = coordenada3  # declaramos los puntos: x tres, y tres, z tres
    x4, y4, z4 = coordenada4  # declaramos los puntos: x cuatro, y cuatro, z cuatro

    matriz_a = [
        [x2 - x1, y2 - y1, z2 - z1],
        [x3 - x1, y3 - y1, z3 - z1],
        [x4 - x1, y4 - y1, z4 - z1],
    ]

    # Calculamos el determinante de la matriz A
    det_a = (
        matriz_a[0][0]
        * (matriz_a[1][1] * matriz_a[2][2] - matriz_a[1][2] * matriz_a[2][1])
        - matriz_a[0][1]
        * (matriz_a[1][0] * matriz_a[2][2] - matriz_a[1][2] * matriz_a[2][0])
        + matriz_a[0][2]
        * (matriz_a[1][0] * matriz_a[2][1] - matriz_a[1][1] * matriz_a[2][0])
    )

    volumen = (
        abs(det_a) / 6.0
    )  # Se calcula el volumen del tetraedro del determinanante entre 6
    return volumen  # Retorna el valor del volumen


# Solicitar las coordenadas de los vértices del tetraedro al usuario
def coor_tetraedro():
    coordtetraedro = []
    for i in range(
        4
    ):  # Se inicia un bucle for que solicita al usurario ingresar las coordenadas
        coord = tuple(
            map(
                float,
                input(
                    f"Ingrese las coordenadas del vértice {i+1} (x, y, z): "
                ).split(  # Se solicita la entrada  al usuario y aca lo divide en separadores con un "," ejemplo 0, 0
                    ", "
                ),
            )
        )
        coordtetraedro.append(coord)  # agrega la coordenada a la lista
    return coordtetraedro  # Y aqui retornaria las coordenadas ingresadas por el usuario


# Solicitar las coordenadas de los vértices del tetraedro al usuario
coordPoligono = coor_tetraedro()

# Calcular y mostrar el volumen del tetraedro
if (
    len(coordPoligono) == 4
):  # Aqui se mide el numero de caracteres que sea igual a 4 para poder cumplir con la condicion
    voltetraedro = calcular_volumen_tetraedro(*coordPoligono)
    print(
        f"El volumen del tetraedro con vértices {coordPoligono} es: {voltetraedro}"  # Aqui se imprime el volumen del tetraedro
    )
else:
    print(
        "Se requiere los 4 vertices para calcular el volumen de un tetraedro."
    )  # Se imprime un mensaje indicando que se necesitan mas de 3 coordenadas para poder hallar un area
