from determinante import determinante
from leer_matriz import leer, pintar_matriz
from matriz_adjunta import inversa_adjunta
from matriz_inversa import inversa
from sistema_cramer import resolver_sistema
from colinealidad import areaTriangulo
import time


def barraProgreso():
    print("Instalando virus por favor espere...")
    barra = "-" * 50
    char = "*"

    for i in range(100):
        x = list(barra)
        x[i // 2] = char
        barra = "".join(x)
        print(f"[{barra}] {i+1}%", end="\r")
        time.sleep(0.04)
    print("\nVirus instalado con exito.", end="\n\n")


def menu():
    opcion = ""
    while opcion != "9":
        mostrarMenu()
        opcion = input("\nIngrese una opcion: ")
        ejecutar(opcion)


def mostrarMenu():
    menu = """     1. Calcular la inversa de una matriz  mediante Gauss-Jordan.
            2. Calcular la inversa de una matriz mediante matriz adjunta.
            3. Calcular el determinante de una matriz.
            4. Resolución de un sistema de ecuaciones por Cramer.
            5. Resolución de un sistema de ecuaciones por matriz inversa.
            6. Cálculo de colinealidad de tres puntos en el plano.
            7. Cálculo de área de un triángulo.
            8. Cálculo de volumen de un tetraedro.
            9. Salir"""
    print(menu)


def ejecutar(opcion):
    match opcion:
        case "1":
            matriz = leer()
            print("La inversa es...")
            matriz_inversa = inversa(matriz)
            # barraProgreso()
            pintar_matriz(matriz_inversa)
        case "2":
            matriz = leer()
            print("La inversa de la matriz por la matriz adjunta es...")
            inversa = inversa_adjunta(matriz)
            if inversa is not None:
                pintar_matriz(inversa)
            else:
                print("No tiene inversa")
            pass
        case "3":
            matriz = leer()
            print("El determinante es...")
            # barraProgreso()
            numero = determinante(matriz)
            barraProgreso()
            print(f"El determinante es {numero}")
        case "4":
            matriz_ecuacion = leer()
            resolucion = resolver_sistema(matriz_ecuacion)
            pintar_matriz(resolucion)
        case "5":
            matriz_ec = leer()
            solucion = inversa(matriz_ec)
            pintar_matriz(solucion)
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            print("Gracias por usar la aplicacion")


menu()
