# crear una funcion para calcular la matriz adjunta de una matriz dada.
"""
Para calcular la inversa de una matriz mediante el método de la matriz adjunta,
se determina la matriz de cofactores, se calcula su transpuesta para obtener la matriz adjunta,
y luego se divide cada elemento de la matriz adjunta por el determinante de la matriz original,
siempre y cuando este último sea distinto de cero.
"""


# Definir una función que calcule el menor de una matriz dado sus índices i y j
def menor(matriz, i, j):
    # Obtenemos el numero de filas de la matriz
    n = len(matriz)

    # Creamos una lista para almacenar el menor
    menor_matriz = []

    # Iteramos para crear el menor
    for k in range(n):
        if k != i:
            menor_matriz.append([])
            for l in range(n):
                if l != j:
                    menor_matriz[-1].append(matriz[k][l])

    return menor_matriz


# Definimos la funcion que calcula los cofactores de una matriz
def cofactor(matriz, i, j):
    # Obtenemos el numero de filas de la matriz
    n = len(matriz)

    # Calculamos el menor de la matriz
    menor_matriz = menor(matriz, i, j)

    # Calculamos el cofactor
    cofactor_matriz = (-1) ** (i + j) * determinante(menor_matriz)

    return cofactor_matriz


# Definimos la funcion que calcula la determinante de una matriz
def determinante(matriz):
    # Obtenemos el numero de filas de la matriz
    n = len(matriz)

    # Verificamos si la matriz es de tamaño 1x1
    if n == 1:
        # Retornamos el único elemento de la matriz
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(n):
            det += ((-1) ** i) * matriz[0][i] * determinante(menor(matriz, 0, i))
        return det


# Definimos la función que calcula la inversa de una matriz mediante la matriz adjunta
def inversa_adjunta(matriz):
    # Obtenemos el numero de filas de la matriz
    n = len(matriz)

    # Calculamos el determinante de la matriz
    det = determinante(matriz)

    # Verificamos si la matriz tiene inversa
    if det == 0:
        print("La matriz no tiene inversa.")
        return None

    # Calculamos la matriz adjunta
    adjunta = []
    for i in range(n):
        adjunta.append([])
        for j in range(n):
            adjunta[i].append(cofactor(matriz, j, i))

    # Calculamos la inversa multiplicando la matriz adjunta por el inverso del determinante
    inversa = [[adjunta[i][j] / det for j in range(n)] for i in range(n)]

    return inversa
