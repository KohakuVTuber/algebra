# crear una funcion que calcule el determinante de una matriz
""" 
Para calcular el determinante de una matriz, se debe tener en cuenta que
el determinante de una matriz de 1x1 es el elemento de la matriz, y el
determinante de una matriz de 2x2 es el producto de la diagonal principal
menos el producto de la diagonal secundaria. Para calcular el determinante
de una matriz de 3x3 o mayor, se debe tener en cuenta que el determinante de
una matriz es igual a la suma de los productos de los elementos de la primera
fila por sus respectivos cofactores. El cofactor de un elemento es igual al determinante
de la matriz que se obtiene al eliminar la fila y la columna del elemento.
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
