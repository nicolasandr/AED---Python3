"""
Un bazar necesita un sistema para gestionar las ventas realizadas. Cada venta realizada está representada por un
código de producto del bazar consiste en un número de 8 dígitos, donde los primeros dos dígitos representan al tipo
de producto (10-Jarras, 11-Alcuzas, etc.).
Además, cuenta con una lista ordenada de códigos de productos que se encuentran en promoción "compre uno, lleve otro
gratis", esto significa que si un cliente compró un producto en promoción, en lugar de una unidad se lleva dos.

Se pide un programa desarrollado en Python, controlado por menú de opciones para cumplir con lo siguiente:

1) Generar una lista de n elementos con los códigos de producto de las ventas realizadas por el bazar (hasta 8 dígitos)
   Ayuda: generar números entre 10.000.000 y 99.999.999 (quedan 90 tipos de producto)
2) Generar la lista de m productos en promoción y ordenar de menor a mayor (m debe ser menor o igual a la mitad de n)
   Ayuda: generar esta lista eligiendo al azar de la lista generada en punto 1.
3) Mostrar en cuánto se redujo el stock por cada tipo de producto (cuánto salió del tipo 10, cuánto del tipo 11, etc.).
   Además, indicar cuál es el tipo de producto que más salió del stock.
"""
import random

from MisFunciones import *


def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Generar lista de ventas de productos")
    print("2. Generar lista de productos en promoción")
    print("3. Mostrar reducción de stock por tipo (y el tipo de producto que más bajó)")
    print("0. SALIR")


def punto1(cant_ventas):
    vec = [0] * cant_ventas
    for i in range(cant_ventas):
        vec[i] = random.randint(10000000, 99999999)
    return vec


def punto2(vv, m):
    vp = [0] * m
    for i in range(m):
        vp[i] = random.choice(vv)
    select_sort_asc(vp)
    return vp


def punto3(vv, vp):
    vconteo = [0] * 90
    for i in range(len(vv)):
        tipo = vv[i] // 1000000
        pos = tipo - 10
        existe = busqueda_binaria_asc(vp, vv[i])
        if existe == -1:
            vconteo[pos] += 1  # No está en promoción
        else:
            vconteo[pos] += 2  # SI está en promoción 2x1
    return vconteo


def principal():
    n = 0
    vec_ven = []
    flag_menu1 = False
    flag_menu2 = False
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese su elección:"))
        if opcion == 1:
            flag_menu1 = True
            n = cargar_mayor_que(1, "\nIngrese la cantidad de ventas aleatorias a generar:")
            vec_ven = punto1(n)
            print("\nSe generó el listado de ventas.")
            print(vec_ven)
        elif opcion == 2:
            # ----------------------------------------------
            if flag_menu1:
                flag_menu2 = True
                m = cargar_entre(0, (n//2),"\nIngrese la cantidad de promociones a generar:")
                vec_2x1 = punto2(vec_ven, m)
                print("\nSe generó el listado de promociones.")
                print(vec_2x1)
            else:
                print("\nPrimero debe generar la lista de ventas!")
            # ----------------------------------------------
        elif opcion == 3:
            # ----------------------------------------------
            if flag_menu2:
                vec_con = punto3(vec_ven, vec_2x1)
                print()
                for i in range(len(vec_con)):
                    if vec_con[i] > 0:
                        print("Tipo:", i+10, "Cantidad:", vec_con[i])
                # FALTA BUSCAR EL TIPO CON MAYOR SALIDA
            elif flag_menu1:
                print("\nPrimero debe generar la lista de productos en promoción!")
            else:
                print("\nPrimero debe generar listas de ventas y productos en promoción!")
            # ----------------------------------------------
        elif opcion == 0:
            pass
        else:
            print("\nLa opción seleccionada es inválida!")


# script principal
if __name__ == '__main__':
    principal()
