# crear una funcion que calcule la inversa de una matriz mediante Gauss-Jordan.
"""
Para calcular la inversa de una matriz por el metodo de Gauss-Jordan, lo que se hace es, recibir una matriz A de nxn y una matriz I de nxn, donde I es la matriz identidad, y se concatenan, es decir, se pone la matriz A y a su derecha la matriz I, y se aplica el metodo de Gauss-Jordan, de tal manera que al final de aplicar el metodo, la matriz A se convierte en la matriz identidad, y la matriz I se convierte en la inversa de la matriz A. 
"""


# Definimos la funcion que calcula la inversa de una matriz
def inversa(A):
    # Obtenemos el numero de filas de la matriz
    n = len(A)
    # Creamos la matriz I, que es la matriz identidad
    I = []

    # Iteramos para crear la matriz identidad
    for i in range(n):
        I.append([])
        for j in range(n):
            if i == j:
                I[i].append(1)
            else:
                I[i].append(0)

    # Concatenamos la matriz A y la matriz I
    for i in range(n):
        for j in range(n):
            A[i].append(I[i][j])

    # Aplicamos el metodo de Gauss-Jordan
    for i in range(n):
        if A[i][i] == 0:
            print("La matriz no tiene inversa")
            return None

        for j in range(n):
            if i != j:
                ratio = A[j][i] / A[i][i]
                for k in range(2 * n):
                    A[j][k] = A[j][k] - ratio * A[i][k]

    # Hacemos que los elementos de la diagonal principal sean 1
    for i in range(n):
        divisor = A[i][i]
        for j in range(2 * n):
            A[i][j] = A[i][j] / divisor

    # Extraemos la matriz inversa
    Inv = []

    for i in range(n):
        Inv.append([])
        for j in range(n):
            Inv[i].append(A[i][j + n])

    return Inv
