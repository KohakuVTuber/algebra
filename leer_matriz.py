def leer():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            numero = int(input(f"Ingrese el numero en la posicion [{i+1}] [{j+1}]: "))
            matriz[i].append(numero)
            pintar_matriz(matriz)
    return matriz


def pintar_matriz(matriz: list):
    for i in matriz:
        print("[ ", end="")
        for numero in i:
            print(numero, end=" ")
        print(" ]")
