import os.path
import pickle
import random
import matplotlib.pyplot as plt
from soporte import *


def validar():
    n = int(input('Ingrese la cantidad de servicios a cargar (mayor a cero): '))
    while n <= 0:
        n = int(input('Error... Se pidió mayor a cero... Ingrese nuevamente la cantidad (mayor a cero): '))
    return n


def visualizar_servicios(vec):
    plt.figure(figsize=(6, 4))
    plt.axis('off')

    y_position = 0.9
    for servicio in vec:
        plt.text(0.5, y_position,
                 f'Nombre: {servicio.codigo}\nID: {servicio.descripcion}\nDNI: {servicio.cliente}\ntipo: {servicio.tipo}\n\nMonto: {servicio.monto}',
                 horizontalalignment='center', verticalalignment='top')
        y_position -= 0.5

    plt.show()


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
    # for servicio in vec:
    visualizar_servicios(vec)
    # print(servicio)


def determinar_cod(vec):
    codigo_encontrado = False

    entrada = int(input('Ingrese el codigo que desea buscar:'))
    for i in range(len(vec)):
        if entrada == vec[i].codigo:
            codigo_encontrado = True
            print(vec[i])
            print('\n')
            if vec[i].tipo > 4:
                vec[i].monto += 100000
                print('\nModificacion por tipo mayor a 4:')
                print(vec[i])
                print('\n')
            break
    if not codigo_encontrado:
        print('el objeto buscado no existe!')


def moto_total_por_servicio(vec):
    acumulador = [0] * 30

    for i in range(len(vec)):
        acumulador[vec[i].tipo - 1] += vec[i].monto

    for i in range(len(acumulador)):
        if acumulador[i] > 0:
            print('El servicio:', i + 1, 'tiene un monto total pagado de:$', acumulador[i])
    return acumulador


def archivo_binario(archivo, vec):
    file_binary = open(archivo, 'wb')
    m = int(input('ingrese valor de un monto:'))
    for objeto in vec:
        if objeto.monto > m:
            pickle.dump(objeto, file_binary)
    file_binary.close()


def existe_archivo_binario(archivo):
    if not os.path.exists(archivo):
        return False
    return True


def mostrar_archivo_binario(archivo):
    file_binary = open(archivo, 'rb')
    monto_total = 0
    cantidad_reg = 0
    while file_binary.tell() < os.path.getsize(archivo):
        registro = pickle.load(file_binary)
        if registro.tipo not in (1, 2):
            print(registro)
            monto_total += registro.monto
            cantidad_reg += 1

    if cantidad_reg == 0:
        print('el promedio es: 0')
    else:
        print('El promedio de todos los montos totales de los registros cargados es:', monto_total / cantidad_reg)
    file_binary.close()


def principal():
    vec = []
    archivo = 'servicio.dat'
    opcion = -1
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
            print("Carga finalizada - Arreglo generado")
            print()

        elif opcion == 2:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                mostrar_arreglo(vec)
                print()

        elif opcion == 3:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # tarea a completar por el alumno
                determinar_cod(vec)

        elif opcion == 4:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                acumulador = moto_total_por_servicio(vec)

        elif opcion == 5:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # tarea a completar por el alumno
                archivo_binario(archivo, vec)
                print('\nse genero archivo binario con exito!')

        elif opcion == 6:
            # tarea a completar por el alumno
            if existe_archivo_binario(archivo):
                mostrar_archivo_binario(archivo)
            else:
                print('No existe archivo binario:', archivo)
        else:
            # tarea a completar por el alumno
            if opcion not in (1, 2, 3, 4, 5, 6, 7):
                print('Debe ingresar un valor valido.')


if __name__ == '__main__':
    principal()
