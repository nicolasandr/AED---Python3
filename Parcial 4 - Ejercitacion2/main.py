import os.path
import pickle

from funciones import *

import random


def menu():
    print("1_ Cargar los datos de n registros de tipo Medicamento en un arreglo de registros (cargue n por teclado).")
    print("2_ Mostrar el arreglo creado en el punto 1, a razón de un registro por línea..")
    print(
        "3_ crear un archivo de registros en el cual se copien los datos de todos los registros cuyo tipo sea 0 o 1 y cuyo importe a facturar sea menor a un valor x que se carga por teclado.")
    print("4_ Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla. ")
    print(
        "5_ Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del medicamento sea igual a nom (cargar nom por teclado). ")
    print(
        "6_ Usando el arreglo creado en el punto 1, determine la cantidad de medicamentos de cada posible tipo por cada posible forma de presentación (o sea, 25 * 10 = 250 contadores en una matriz de conteo).")


def add_in_order(v, x):
    izq, der, pos = 0, len(v) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        if v[medio].num_telefono == x.num_telefono:
            pos = medio
            break
        elif x.num_telefono <= v[medio].num_telefono:
            der = medio - 1
        else:
            izq = medio + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [x]


def crear_arreglo(v):
    cont = 0
    entrada = int(input("\nIngrese la cantidad de registros que desea generar:"))

    while cont <= entrada:
        num_telefono = str(random.randint(100000, 200000))
        hora_de_consumo = random.randint(0, 23)
        tipo_consumo = random.randint(1, 3)
        monto_consumo = random.randint(111111, 2222222)

        registro = Consumo(num_telefono, hora_de_consumo, tipo_consumo, monto_consumo)
        add_in_order(v, registro)
        cont += 1
    return v


def mostrar_arreglo(v):
    for i in v:
        print(i)
    print()


def monto_total(v):
    #  columna : hora consumo     fila : tipo consumo
    mat = [[0] * 24 for _ in range(3)]
    for p in v:
        mat[p.tipo_consumo - 1][p.hora_de_consumo] += p.monto_consumo
    return mat


def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if 0 < j < 12:
                print(" para la hora de consumo:", j , " y el tipo de consumo",i+1,"corresponde un total de:", mat[i][j])


def crear_archivo_binario(v, fdb):
    file_binary = open(fdb, "wb")
    t = input("\nIngrese un numero de telefono:")
    for i in range(len(v)):
        if (v[i].tipo_consumo == 1 or v[i].tipo_consumo == 2) and v[i].num_telefono == t:
            pickle.dump(v[i], file_binary)


def mostrar_archivo(fdb):
    cont = 0
    file_binary = open(fdb, "rb")
    if not os.path.exists(fdb):
        print("El archivo binario no exsite.")
        return
    t = os.path.getsize(fdb)
    while file_binary.tell() < t:
        print(pickle.load(file_binary))
        cont += 1
    print("cantidad total de registros:", cont)


def principal():
    archivo_binario = "consumos.dat"
    entrada = -1
    v = []

    while entrada != 0:
        menu()
        entrada = int(input("Ingrese una opcion:"))
        if entrada == 1:
            v = crear_arreglo(v)
        if entrada == 2:
            mostrar_arreglo(v)
        if entrada == 3:
            mat = monto_total(v)
            mostrar_matriz(mat)

        if entrada == 4:
            crear_archivo_binario(v, archivo_binario)
        if entrada == 5:
            mostrar_archivo(archivo_binario)

        if entrada not in (0, 1, 2, 3, 4, 5, 6):
            print("\ningrese un valor correcto.")


if __name__ == '__main__':
    principal()
