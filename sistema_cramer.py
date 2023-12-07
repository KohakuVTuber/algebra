# crear una funcion para la resolución de un sistema de ecuaciones por Cramer

"""
Para resolver un sistema de ecuaciones lineales mediante la regla de Cramer,
se calcula el determinante principal y los determinantes obtenidos al reemplazar
la columna de coeficientes de cada variable con la columna de constantes,
y las soluciones son las razones de estos determinantes respecto al determinante principal.
"""


# Calcular el determinante de una matriz cuadrada
def determinante(matriz):
    # Dimensión de una matriz
    n = len(matriz)
    # Verificar si la matriz es de tamaño 1x1
    if n == 1:
        # Retorna el único elemento de la matriz
        return matriz[0][0]
    # Verifica si la matriz es de tamaño 2x2
    elif n == 2:
        # Calcula y retonar el determinante de la matriz
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        # Itera sobre la primera fila de la matriz
        for i in range(n):
            # Acumula el determinante
            det += ((-1) ** i) * matriz[0][i] * determinante(submatriz(matriz, 0, i))
        return det


# Define la función submatriz
def submatriz(matriz, fila, columna):
    return [
        # Crea una nueva fila
        fila[:columna] + fila[columna + 1 :]
        # Itera sobre las filas de la matriz original
        for fila in (matriz[:fila] + matriz[fila + i])
    ]


# Define la función de resolver por el sistema de acuaciones
def resolver_sistema(ecuaciones):
    # Obtiene el número de ecuaciones en el sistema y lo almacena
    n = len(ecuaciones)
    # Contiene las filas de las ecuaciones, excluyendo el último elemento de cada fila
    coeficientes = [fila[:-1] for fila in ecuaciones]
    # Contiene el último elemento de cada fila de las ecuaciones
    resultados = [fila[-1] for fila in ecuaciones]
    # Calcular el determinante del sistema principal
    det_principal = determinante(coeficientes)

    # Verifica si el determinante principal es igual a cero
    if det_principal == 0:
        print("La matriz no tiene solución única")
        return None
    # Almacena las soluciones del sistema
    soluciones = []

    # Itera sobre todas las variables del sistema
    for i in range(n):
        # Crear una copia del sistema original
        sistema_temporal = [fila[:] for fila in coeficientes]
        # Itera sobre todas las filas del sistema
        for j in range(n):
            # Reemplazar la columna i con la columna de resultados
            sistema_temporal[j][i] = resultados[j]
        # Calcular el determinante del sistema temporal
        det_temporal = determinante(sistema_temporal)
        # Calcula la solución para la variable i
        solucion_i = det_temporal / det_principal
        # Agrega la solución al final de la lista de soluciones
        soluciones.append(solucion_i)

    # Retorna la lista de soluciones después del calculo
    return soluciones

    # Verifica si la lista de soluciones no está vacía
    if soluciones:
        print("Soluciones del sistema:")
        # Itera sobre la lista de soluciones
        for i, solucion in enumarate(soluciones):
            # Imprime cada solución junto con su variable
            print(f"x{i+1} = {solucion}")
