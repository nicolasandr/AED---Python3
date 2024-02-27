import os.path
import pickle
import random
from soporte import *


def validar():
    n = int(input('Ingrese la cantidad de servicios a cargar (mayor a cero): '))
    while n <= 0:
        n = int(input('Error... Se pidió mayor a cero... Ingrese nuevamente la cantidad (mayor a cero): '))
    return n


def add_in_order(vec, t):
    n = len(vec)
    izq = 0
    der = n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if t.codigo == vec[c].codigo:
            pos = c
            break
        elif t.codigo < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [t]


def cargar_arreglo():
    nombres = ("Juan", "Ana", "Luis", "Carla", "Pedro", "Diana", "Matias", "Sandra", "Jose", "Maria", "Lucas")
    apellidos = ("Perez", "Gomez", "Suarez", "Dimarco", "Franceschi", "Tomasini", "Quispe", "Mamani", "Smith", "Evans")
    vec = []
    n = validar()
    for i in range(n):
        cod = random.randint(1, 99999)
        des = "Servicio " + random.choice("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ") + str(random.randint(1, 9))
        cli = random.choice(nombres) + " " + random.choice(apellidos)
        tip = random.randint(1, 30)
        mon = round(random.uniform(0, 9000000), 2)

        t = Servicio(cod, des, cli, tip, mon)
        add_in_order(vec, t)
    return vec


def mostrar_arreglo(vec):
    print('Listado completo de servicios ofrecidos')
    for servicio in vec:
        print(servicio)


def buscar_codigo_identificacion(vec):
    existe_objeto = False
    cod = int(input('\nIngrese el codigo de inteficacion a buscar:'))
    for objeto in vec:
        if cod == objeto.codigo:
            print(objeto)
            existe_objeto = True
            if objeto.tipo > 4:
                objeto.monto += 100000
                print('objeto modificado:', objeto)
            break

    if not existe_objeto:
        print('\nEl objeto buscado no existe.')


def monto_total_acumulado(vec):
    acumulador = [0] * 30
    for objeto in vec:
        acumulador[objeto.tipo - 1] += objeto.monto

    for i in range(len(acumulador)):
        if acumulador[i] != 0:
            print('El monto acumulado para el servicio:', i + 1, 'es:', acumulador[i])


def grabar_archivo_binario(archivo, vec):
    file_binary = open(archivo, 'wb')
    m = int(input('\nIngrese un valor para filtrar monto total:'))
    for objeto in vec:
        if m < objeto.monto:
            pickle.dump(objeto, file_binary)
    file_binary.close()


def mostrar_archivo_generado(archivo):
    cont = 0
    montos_totales = 0
    if not os.path.exists(archivo):
        print('no existe el archivo:', archivo)
    else:
        file_binary = open(archivo, 'rb')
        while file_binary.tell() < os.path.getsize(archivo):
            objeto = pickle.load(file_binary)
            if objeto.tipo not in (1, 2):
                print(objeto)
                montos_totales += objeto.monto
                cont += 1
    if cont == 0:
        print('\n No hay registros filtrados.')
    else:
        promedio = montos_totales // cont
        print('\nEl promedio es:', promedio)


def principal():
    vec = []
    archivo = 'servicio.dat'
    opcion = -1
    arreglo_generado = False
    while opcion != 7:
        print('----------------------- Menú de opciones - Servicios Agropecuarios -------------------------')
        print('1. Cargar arreglo (ordenado por código de servicio)')
        print('2. Mostrar arreglo completo')
        print('3. Buscar por código de servicio')
        print('4. Conteo por tipo de servicio')
        print('5. Generar archivo con condición de filtro')
        print('6. Mostrar archivo (incluir promedio al final)')
        print('7. Salir')
        print('--------------------------------------------------------------------------------------------')
        opcion = int(input('Ingrese número de opción: '))

        if opcion == 1:
            vec = cargar_arreglo()
            arreglo_generado = True
            print("Carga finalizada - Arreglo generado")
            print()

        elif opcion == 2 and arreglo_generado:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                mostrar_arreglo(vec)
                print()

        elif opcion == 3 and arreglo_generado:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # tarea a completar por el alumno
                buscar_codigo_identificacion(vec)

        elif opcion == 4 and arreglo_generado:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # tarea a completar por el alumno
                monto_total_acumulado(vec)

        elif opcion == 5 and arreglo_generado:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # tarea a completar por el alumno
                grabar_archivo_binario(archivo, vec)

        elif opcion == 6:
            # tarea a completar por el alumno
            mostrar_archivo_generado(archivo)

        else:
            # tarea a completar por el alumno
            if opcion not in ( 1, 2, 3, 4, 5, 6,7):
                print('\nDebe ingresar un valor valido para opcion.')


if __name__ == '__main__':
    principal()
