from funciones import *


def menu():
    print(20 * '-')
    print('Menu principal:')
    print('\n1_generar vector de objetos.')
    print('2_Listar todas las entradas vendidas en un dia ingresado por teclado.')
    print('3_Determinar el total vendido por cada tipo de proyeccion y clasificacion de la pelicula(matriz)')
    print(
        '4_Grabar en un archivo de texto el nombre de la pelicula y la clasificacion de toda las ventas por un tipo de proyeccion(ingresada por teclado)')
    print('5_Determinar cual tipo de proyeccion recaudo mas en el mes.')
    print(
        '6_Grabar en un segundo archivo las ventas de entradas por un dia (d) y ua clasificacion(c) ambos ingresados por teclado.\n')
    print('0_para finalizar')


def add_in_order(objeto, vector):
    izq, der, pos = 0, len(vector) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        if objeto.numero == vector[medio].numero:
            pos = medio
            break
        elif objeto.numero <= vector[medio].numero:
            der = medio - 1
        else:
            izq = medio + 1

    if izq > der:
        pos = izq
    vector[pos:pos] = [objeto]


def generar_vector(arreglo_registros, fb):
    file_binary = open(fb, 'rb')
    while file_binary.tell() < os.path.getsize(fb):
        objeto = pickle.load(file_binary)
        add_in_order(objeto, arreglo_registros)
    file_binary.close()


def mostrar_vector(v):
    for objeto in v:
        print(objeto)


def principal():
    entrada = -1
    arreglo_registros = []
    fb = 'tickets.dat'

    while entrada != 0:
        menu()
        entrada = int(input('\nIngrese una opcion por teclado:'))
        if entrada == 1:
            generar_vector(arreglo_registros, fb)
            mostrar_vector(arreglo_registros)
        elif entrada == 2:
            pass     
        elif entrada == 3:
            pass
        elif entrada == 4:
            pass
        elif entrada == 5:
            pass
        elif entrada == 6:
            pass
        elif entrada not in (1, 2, 3, 4, 5, 6, 0):
            print('\nDebe ingresar un valor valido.')


if __name__ == '__main__':
    archivo()
    principal()
