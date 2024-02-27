import random

from funciones import *


def opcion1(arreglo_registros, n):
    nombres = ["nico", "laura", "javier"]
    cont = 0
    # generar registros aleatorios:
    while True:
        if cont == n:
            break
        dni = random.randint(100, 10000)
        nombre = random.choice(nombres)
        cargo = random.randint(0, 19)  # codigo del (0 a 19)
        puntaje = random.randint(0, 100)

        arreglo_registros.append(Concursante(dni, nombre, cargo, puntaje))
        cont += 1


def cantidad_cargos(arreglo_registros):
    cont = [0] * 20

    for i in range(len(arreglo_registros)):
        cont[arreglo_registros[i].cargo] += 1

    for i in range(len(cont)):
        print("cargo:", i, "=", cont[i])


def imprimir(arreglo_registros):
    vacio = True
    for i in range(len(arreglo_registros)):
        if arreglo_registros[i].puntaje >= 70:
            print(arreglo_registros[i])
            vacio = False
    if vacio:
        print("Ninguno de los concursantes logro promedio mayor a 70%")


def ordenamiento(arreglo_registros):
    n = len(arreglo_registros)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arreglo_registros[i].puntaje > arreglo_registros[j].puntaje:
                arreglo_registros[i].puntaje, arreglo_registros[j].puntaje = arreglo_registros[j].puntaje,arreglo_registros[i].puntaje

    for i in range(len(arreglo_registros)):
        print(arreglo_registros[i])

def principal():
    entro_a_opcion1 = False
    arreglo_registros = []

    n = int(input("ingrese la cantidad de registros que desee cargar:"))

    while True:
        menu()
        entrada = int(input("ingrese una opcion:"))
        if entrada == 1:
            opcion1(arreglo_registros, n)
            entro_a_opcion1 = True
        elif entrada == 2 and entro_a_opcion1:
            imprimir(arreglo_registros)
        elif entrada == 3 and entro_a_opcion1:
            cantidad_cargos(arreglo_registros)
        elif entrada == 4 and entro_a_opcion1:
            ordenamiento(arreglo_registros)
        elif entrada == 0:
            break


if __name__ == '__main__':
    principal()
