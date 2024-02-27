"""
Un bazar necesita un sistema para gestionar las ventas realizadas. Cada venta realizada está representada por un
código de producto del bazar consiste en un número de 8 dígitos, donde los primeros dos dígitos representan al tipo
de producto (10-Jarras, 11-Alcuzas, etc.).
Además, cuenta con una lista ordenada de códigos de productos que se encuentran en promoción "compre uno, lleve otro
gratis", esto significa que si un cliente compró un producto en promoción, en lugar de una unidad se lleva dos.

Se pide un programa desarrollado en Python, controlado por menú de opciones para cumplir con lo siguiente:

1) Generar una lista de n elementos con los códigos de producto de las ventas realizadas por el bazar (hasta 8 dígitos)
   Ayuda: generar números entre 10.000.000 y 99.999.999 (quedan 90 tipos de producto)
2) Generar la lista de m productos en promoción y ordenar de menor a mayor (m debe ser menor a la mitad de n)
   Ayuda: generar esta lista eligiendo al azar de la lista generada en punto 1.
3) Mostrar en cuánto se redujo el stock por cada tipo de producto (cuánto salió del tipo 10, cuánto del tipo 11, etc.).
   Además, indicar cuál es el tipo de producto que más salió del stock.
"""

from MisFunciones import *


def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Generar lista de ventas de productos")
    print("2. Generar lista de productos en promoción")
    print("3. Mostrar reducción de stock por tipo (y el tipo de producto que más bajó)")
    print("0. SALIR")


def principal():
    flag_menu1 = False
    flag_menu2 = False
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese su elección:"))

        if opcion == 1:
            flag_menu1 = True
            vec_ven = []
            n = cargar_mayor_que(0, "\nIngrese la cantidad de ventas aleatorias a generar:")
            # completar punto 1
        elif opcion == 2:
            # ----------------------------------------------
            if flag_menu1:
                flag_menu2 = True
                # completar punto 2
            else:
                print("\nPrimero debe generar la lista de ventas!")
            # ----------------------------------------------
        elif opcion == 3:
            # ----------------------------------------------
            if flag_menu2:
                pass
                # completar punto 3
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
