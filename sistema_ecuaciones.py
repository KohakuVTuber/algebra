# Definir una función para calcular el determinante de una matriz
def determinante(matriz):
    # Obtener la dimensión de la matriz
    n = len(matriz)

    # Caso base: si la matriz es de 1x1, el determinante es el único elemento
    if n == 1:
        return matriz[0][0]

    # Caso base: si la matriz es de 2x2, el determinante es la diferencia de los productos de las diagonales
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    # Caso general: si la matriz es de nxn, el determinante se calcula usando la expansión por cofactores
    else:
        # Inicializar una variable para almacenar el determinante
        det = 0

        # Recorrer la primera fila de la matriz
        for j in range(n):
            # Obtener el elemento de la primera fila y la columna j
            elemento = matriz[0][j]
            # Obtener la submatriz que se forma al eliminar la primera fila y la columna j
            submatriz = [fila[:j] + fila[j + 1 :] for fila in matriz[1:]]
            # Calcular el cofactor correspondiente al elemento
            cofactor = (-1) ** (j) * determinante(submatriz)
            # Sumar el producto del elemento y el cofactor al determinante
            det += elemento * cofactor

        # Devolver el determinante
        return det


# Definir una función para calcular la matriz de cofactores de una matriz
def cofactores(matriz):
    # Obtener la dimensión de la matriz
    n = len(matriz)

    # Inicializar una matriz vacía para almacenar los cofactores
    matriz_cof = []

    # Recorrer las filas de la matriz
    for i in range(n):
        # Inicializar una lista vacía para almacenar los cofactores de la fila i
        fila_cof = []

        # Recorrer las columnas de la matriz
        for j in range(n):
            # Obtener la submatriz que se forma al eliminar la fila i y la columna j
            submatriz = [
                fila[:j] + fila[j + 1 :] for fila in matriz[:i] + matriz[i + 1 :]
            ]
            # Calcular el cofactor correspondiente al elemento i,j
            cofactor = (-1) ** (i + j) * determinante(submatriz)
            # Agregar el cofactor a la lista de la fila i
            fila_cof.append(cofactor)

        # Agregar la lista de cofactores de la fila i a la matriz de cofactores
        matriz_cof.append(fila_cof)

    # Devolver la matriz de cofactores
    return matriz_cof


# Definir una función para calcular la matriz adjunta de una matriz
def adjunta(matriz):
    # Obtener la matriz de cofactores de la matriz
    matriz_cof = cofactores(matriz)
    # Obtener la matriz transpuesta de la matriz de cofactores
    matriz_adj = list(zip(*matriz_cof))
    # Devolver la matriz adjunta
    return matriz_adj


# Definir una función para calcular la matriz inversa de una matriz
def inversa(matriz):
    # Obtener el determinante de la matriz
    det = determinante(matriz)
    # Verificar que el determinante no sea cero
    if det == 0:
        # Si el determinante es cero, la matriz no tiene inversa
        return None
    else:
        # Si el determinante no es cero, la matriz tiene inversa
        # Obtener la matriz adjunta de la matriz
        matriz_adj = adjunta(matriz)
        # Obtener la matriz inversa dividiendo cada elemento de la matriz adjunta por el determinante
        matriz_inv = [[elemento / det for elemento in fila] for fila in matriz_adj]
        # Devolver la matriz inversa
        return matriz_inv


""" Caso de uso pa edu y su menu """
# Definir el sistema de ecuaciones como una matriz de coeficientes y un vector de términos independientes
# Por ejemplo: 2x + 3y = 5, x - y = 1
A = [[2, 3], [1, -1]]  # Matriz de coeficientes
b = [5, 1]  # Vector de términos independientes

# Calcular la matriz inversa de A usando la función inversa
A_inv = inversa(A)

# Verificar que la matriz inversa exista
if A_inv is None:
    # Si la matriz inversa no existe, el sistema no tiene solución única
    print("El sistema no tiene solución única")
else:
    # Si la matriz inversa existe, el sistema tiene solución única
    # Multiplicar la matriz inversa de A por el vector b para obtener el vector de soluciones
    x = [sum(a * b for a, b in zip(fila, b)) for fila in A_inv]
    # Imprimir el vector de soluciones
    print(x)
