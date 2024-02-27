import random

from funciones import *


def cargar_arreglo(arreglo_registros, n):
    nombre_trabajo = ["limpiar casa", "limpiar baños", "limpieza de pasillos"]
    cont = 0
    while True:
        if n == cont:
            break
        id = random.randint(0, 1000)
        nombre = random.choice(nombre_trabajo)
        tipo = random.randint(0, 3)
        importe = random.randint(10000, 50000)
        cantidad_de_personal = random.randint(3, 10)

        arreglo_registros.append(Trabajo(id, nombre, tipo, importe, cantidad_de_personal))
        cont += 1


def ordenamiento(arreglo_registros):
    n = len(arreglo_registros)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arreglo_registros[i].importe < arreglo_registros[j].importe:
                arreglo_registros[i], arreglo_registros[j] = arreglo_registros[j], arreglo_registros[i]

    return arreglo_registros


def mostrar_arreglo(arreglo_registros):
    print("\n")
    arreglo_ordenado = ordenamiento(arreglo_registros)
    for i in range(len(arreglo_ordenado)):
        print("Trabajo N", i, ":", arreglo_registros[i])
    print("\n")


def mayor_cantidad_personal(arreglo_registros):
    mayor = None
    for i in range(len(arreglo_registros)):
        if mayor is None or arreglo_registros[i].cantidad_de_personal > mayor:
            mayor = arreglo_registros[i].cantidad_de_personal

    for i in range(len(arreglo_registros)):
        if mayor == arreglo_registros[i].cantidad_de_personal:
            print("El trabajo con mayor cantidad de personal afectado es:", arreglo_registros[i])


def buscador(arreglo_registros):
    descripcion_entrada = input("ingrese descripcion o nombre del trabajo para ver si existe en el sistema:")
    existe = False
    for i in range(len(arreglo_registros)):
        if descripcion_entrada == arreglo_registros[i].nombre:
            print("existe el trabajo: ", arreglo_registros[i])
            existe = True
            break

    if not existe:
        print("\nel trabajo no existe en el sistema.\n")


def trabajoportipo(arreglo_registros):
    cant = [0] * 4
    tipo = ["interior", "exterior", "piletas", "tapizados"]

    for i in range(len(arreglo_registros)):
        cant[arreglo_registros[i].tipo] += 1

    for i in range(len(cant)):
        print(tipo[i], ":", cant[i])


def principal():
    arreglo_registros = []
    entro_opcion_1 = False
    print("Bienvenidos al sistema de trabajos:")
    n = int(input("Ingrese el un valor numerico indicando la cantidad de trabajos ofrecidos: "))
    while True:
        menu()
        opcion = int(input("\nIngrese una opcion: "))
        if opcion == 1:
            cargar_arreglo(arreglo_registros, n)
            entro_opcion_1 = True
            print("se cargo el arreglo correctamente!\n")
        elif opcion == 2 and entro_opcion_1:
            mostrar_arreglo(arreglo_registros)
        elif opcion == 3 and entro_opcion_1:
            mayor_cantidad_personal(arreglo_registros)
        elif opcion == 4 and entro_opcion_1:
            buscador(arreglo_registros)
        elif opcion == 5 and entro_opcion_1:
            trabajoportipo(arreglo_registros)
        elif opcion != 0 and entro_opcion_1 == False:
            print("primero debe cargar opcion 1.")
        elif opcion == 0:
            break


if __name__ == '__main__':
    principal()
