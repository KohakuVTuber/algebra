# crear una funcion para la resolución de un sistema de ecuaciones por Cramer

"""
Para resolver un sistema de ecuaciones lineales mediante la regla de Cramer,
se calcula el determinante principal y los determinantes obtenidos al reemplazar
la columna de coeficientes de cada variable con la columna de constantes,
y las soluciones son las razones de estos determinantes respecto al determinante principal.
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


# Definimos la función para resolver un sistema de ecuaciones lineales mediante la regla de Cramer
def resolver_sistema_cramer(coeficientes, constantes):
    # Obtenemos el tamaño del sistema
    n = len(coeficientes)

    # Calculamos el determinante principal
    det_principal = determinante(coeficientes)

    # Verificamos si el determinante es cero
    if det_principal == 0:
        raise ValueError("El sistema no tiene solución única (determinante igual a cero).")

    # Inicializamos una lista para almacenar las soluciones
    soluciones = []

    # Iteramos sobre las variables del sistema
    for i in range(n):
        # Creamos una copia de la matriz de coeficientes para no modificar la original
        matriz_temporal = [fila[:] for fila in coeficientes]

        # Reemplazamos la columna i con la columna de constantes
        for j in range(n):
            matriz_temporal[j][i] = constantes[j]

        # Calculamos el determinante para esta configuración
        det_actual = determinante(matriz_temporal)

        # Calculamos la solución usando la regla de Cramer
        solucion_i = det_actual / det_principal
        soluciones.append(solucion_i)

    return soluciones
