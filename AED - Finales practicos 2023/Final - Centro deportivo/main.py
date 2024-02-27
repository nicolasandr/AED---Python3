import os
import pickle

from soporte import *
import random


def menu():
    print('-' * 50)
    print('Menu principal:')
    print('0_Para finalizar.')
    print('1_generar registros.')
    print('2_mostrar los registros.')
    print('3_determinar monto acumulado.')
    print('4_determinar canidad de deportistas por cada deporte y tipo de beca.')
    print('5_buscar deportista por nombre.')
    print('6_crear archivo binario.')
    print('7_mostrar archivo binario')


def add_in_order(objeto, vec):
    # ordenar por nombre de deportista
    izq, der, pos = 0, len(vec) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        if objeto.nombre == vec[medio].nombre:
            pos = medio
            break
        elif objeto.nombre <= vec[medio].nombre:
            der = medio - 1
        else:
            izq = medio + 1

    if izq > der:
        pos = izq
    vec[pos:pos] = [objeto]


def generar_registros(vec):
    nombres = ('nicolas', 'lucas', 'gustavo', 'sergio', 'mauricio')
    n = input('\nIngrese la cantidad de registros que desea generar:')
    while not n.isdigit():
        n = input('\nIngrese un valor numerico:')

    for _ in range(int(n)):
        id = random.randint(100, 999)
        nombre = random.choice(nombres)
        tipo_deporte = random.randint(0, 49)
        tipo_beca = random.randint(0, 9)
        monto_beca = round(random.uniform(1000, 2000), 2)
        objeto = Deportista(id, nombre, tipo_deporte, tipo_beca, monto_beca)
        add_in_order(objeto, vec)

    print('\nSe genero el arreglo de registros.')


def mostrar_registros(vec):
    for objeto in vec:
        print(objeto)


def acumulador_de_montos(vec):
    acumulador = [0] * 10
    for objeto in vec:
        acumulador[objeto.tipo_beca] += objeto.monto_beca

    for i in range(len(acumulador)):
        if acumulador[i] != 0:
            print('El monto acumulado para el tipo de beca:', i, 'es:', acumulador[i])


def cantidad_deportistas_por_deporte_y_beca(vec):
    mat_cont = [[0] * 50 for _ in range(10)]
    for objeto in vec:
        mat_cont[objeto.tipo_beca][objeto.tipo_deporte] += 1

    for i in range(len(mat_cont)):
        # tipo_deporte
        for j in range(len(mat_cont[0])):
            if mat_cont[i][j] != 0:
                print('cantidad de deportistas para el deporte', j, 'y tipo de beca:', i, 'es:', mat_cont[i][j])


def busqueda_binaria_nombre(vec):
    izq, der = 0, len(vec) - 1
    nombre = input('\nIngrese el nombre del deportista que desea buscar:')
    while izq <= der:
        medio = (izq + der) // 2
        if nombre == vec[medio].nombre:
            return medio
        elif nombre <= vec[medio].nombre:
            der = medio - 1
        else:
            izq = medio + 1
    return 0


def crear_archivo_binario(vec, archivo):
    file_binary = open(archivo, 'wb')
    for objeto in vec:
        if objeto.tipo_beca != 0:
            pickle.dump(objeto, file_binary)
    file_binary.close()

    if not os.path.exists(archivo):
        print('\nEl archivo no se pudo generar.')
    else:
        print('\nEl archivo binario se creo correctamente.')


def mostrar_archivo(archivo):
    monto_acumulado = 0
    if not os.path.exists(archivo):
        print('\nEl archivo:', archivo, 'No existe.')
    else:
        file_binary = open(archivo, 'rb')
        while file_binary.tell() < os.path.getsize(archivo):
            objeto = pickle.load(file_binary)
            print(objeto)
            monto_acumulado += objeto.monto_beca
        file_binary.close()
        print('\nMonto acumulado pagado por los deportistas mostrados:', monto_acumulado)
        

def principal():
    vec = []
    entrada = -1
    archivo = 'archivo.dat'
    existe_arreglo = False
    while entrada != 0:
        menu()
        entrada = int(input('\nIngrese una opcion:'))
        if entrada == 1:
            generar_registros(vec)
            existe_arreglo = True
        elif entrada == 2 and existe_arreglo:
            mostrar_registros(vec)
        elif entrada == 3 and existe_arreglo:
            acumulador_de_montos(vec)
        elif entrada == 4 and existe_arreglo:
            cantidad_deportistas_por_deporte_y_beca(vec)
        elif entrada == 5 and existe_arreglo:
            indice = busqueda_binaria_nombre(vec)
            if indice == 0:
                print('\nNo existe el nombre del deportista en los registros.')
            else:
                print('datos del deportista:', vec[indice])
        elif entrada == 6 and existe_arreglo:
            crear_archivo_binario(vec, archivo)
        elif entrada == 7:
            mostrar_archivo(archivo)
        elif not existe_arreglo:
            print('\nPrimero debe crear los registros.')
        elif entrada not in (0, 1, 2, 3, 4, 5, 6, 7):
            print('\nIngrese una opcion valida.!')


if __name__ == '__main__':
    principal()
