import os
import pickle
from soporte import *

import random


def menu():
    print('-' * 20)
    print('Menu principal:')
    print('0_Para salir.')
    print('1_Generar arreglo de registros.')
    print('2_mostrar datos del arreglo.')
    print('3_Determinar si existe paquete.')
    print('4_Determinar cantidad de paquetes entre medio de trasporte y destino')
    print('5_Determinar monto acumulado que haya pagado el cliente.')
    print('6_Crear archivo binario.')
    print('7_mostrar archivo generado en el punto 7')


def add_in_order(vec, objeto):
    izq, der, pos = 0, len(vec) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        if objeto.id == vec[medio].id:
            pos = medio
            break
        elif objeto.id <= vec[medio].id:
            der = medio - 1
        else:
            izq = medio + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [objeto]


def generar_arreglo():
    arreglo_registros = []
    titulos = ('jujuy', 'salta', 'tucuman', 'cordoba', 'bariloche')
    nombres = ('nicolas', 'carlos', 'julian', 'pablo', 'marcos')
    n = input('\nIngrese la cantidad de registros que desea generar:')
    while not n.isdigit():
        n = input('\nEl valor ingresado debe ser tipo numerico:')

    for _ in range(int(n)):
        id = random.randint(100, 999)
        titulo = random.choice(titulos)
        transporte = random.randint(0, 9)
        monto = round(random.uniform(1000, 2000), 2)
        destino = random.randint(1, 50)
        cliente = random.choice(nombres)
        paquete = Paquete(id, titulo, transporte, monto, destino, cliente)
        add_in_order(arreglo_registros, paquete)
    print('\nSe generaron los registros con exito!')
    return arreglo_registros


def mostrar_registros(vec):
    cont = 0
    for objeto in vec:
        print(objeto)
        cont += 1
    print('\nSe mostraron en total:', cont, 'registros.')


def buscar_titulo(vec):
    existe_titulo = False
    tit = input('\nIngrese el titulo que desea buscar:')
    for objeto in vec:
        if tit == objeto.titulo:
            print('\nEl numero de identificacion del paquete es:', objeto.id)
            print('El cliente que compro el paquete es:', objeto.cliente)
            existe_titulo = True
            break
    if not existe_titulo:
        print('\nNo existe el paquete con ese titulo.')


def cantidad_de_paquetes(vec):
    # destino        transporte
    mat_cont = [[0] * 50 for _ in range(10)]
    for i in vec:
        mat_cont[i.transporte][i.destino - 1] += 1

    for i in range(len(mat_cont)):
        for j in range(len(mat_cont[0])):
            if mat_cont[i][j] != 0:
                print('hay', mat_cont[i][j], ' paquetes para el transporte:', i, 'y el destino:', j + 1)


def monto_acumulado(vec):
    pagos_acumulados = 0
    existe_cliente = False
    nombre = input('\nIngrese nombre del cliente:')
    for objeto in vec:
        if nombre == objeto.cliente:
            pagos_acumulados += objeto.monto
            existe_cliente = True

    if not existe_cliente:
        print('\nEl cliente no existe en los registros.')
    else:
        print('\nLos pagos acumulados de:', nombre, 'son:', round(pagos_acumulados, 2))


def archivo_binario(archivo, vec):
    file_binary = open(archivo, 'wb')
    for objeto in vec:
        # el valor original es 100000, a modo de practica se cambio a 1000
        if objeto.monto > 1000:
            pickle.dump(objeto, file_binary)
    file_binary.close()
    if not os.path.exists(archivo):
        print('\nNo se pudo generar el archivo binario.')
    else:
        print('\nSe genero el archivo binario correctamente.')


def mostrar_archivo(archivo):
    monto_acum = 0
    if not os.path.exists(archivo):
        print('\nNo existe el archivo:', archivo)
    else:
        file_binary = open(archivo, 'rb')
        while file_binary.tell() < os.path.getsize(archivo):
            objeto = pickle.load(file_binary)
            print(objeto)
            monto_acum += objeto.monto
        file_binary.close()
        print('\nMonto acumulado de los registros mostrados:', round(monto_acum, 2))


def principal():
    vec = []
    entrada = -1
    archivo = 'paquetes.dat'
    existe_registros = False
    while entrada != 0:
        menu()
        entrada = int(input('\nSeleccione una opcion:'))
        if entrada == 1:
            vec = generar_arreglo()
            existe_registros = True
        elif entrada == 2 and existe_registros:
            mostrar_registros(vec)
        elif entrada == 3 and existe_registros:
            buscar_titulo(vec)
        elif entrada == 4 and existe_registros:
            cantidad_de_paquetes(vec)
        elif entrada == 5 and existe_registros:
            monto_acumulado(vec)
        elif entrada == 6 and existe_registros:
            archivo_binario(archivo, vec)
        elif entrada == 7:
            mostrar_archivo(archivo)
        elif not existe_registros:
            print('\nPrimero debe cargar los registros!')
        elif entrada not in (0, 1, 2, 3, 4, 5, 6, 7):
            print('\nIngrese un valor correcto de opciones.!')


if __name__ == '__main__':
    principal()
