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


def add_in_buscar(vec, cod):
    n = len(vec)
    izq = 0
    der = n - 1
    pos = - 1
    while izq <= der:
        c = (izq + der) // 2
        if cod == vec[c].codigo:
            pos = c
            break
        elif cod < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    return pos


def acumulador_vec(vec):
    acu = [0] * 30

    for t in vec:
        acu[t.tipo - 1] += t.monto

    for t in range(len(acu)):
        if acu[t] > 0:
            print(f'Para el tipo de servicio {[t + 1]} la cantidad es: $ {round(acu[t], 2)}')


def generar_archivo(archivo, vec):
    mo = float(input('\033[1;36mIngrese un importe para generar el archivo: \033[m'))
    m = open(archivo, 'wb')
    for i in vec:
        if i.monto > mo:
            pickle.dump(i, m)

    m.close()

def calcular_promedio(suma, contador):
    prom = 0
    if contador > 0:
        prom = suma / contador
    return prom


def mostrar_archivo(archivo):
    m = open(archivo, 'rb')
    tam = os.path.getsize(archivo)
    suma = 0
    contador = 0
    while m.tell() < tam:
        envio = pickle.load(m)
        if envio.tipo > 2: #ni 1 ni 2
            contador += 1
            suma += envio.monto
            print(envio)

        promedio = calcular_promedio(suma, contador)

    print('\033[1;35mEl promedio del monto total mostrado es: $ \033[m', round(promedio, 2))
    print()
    print('\033[1;35mLa cantidad de registros mostrados es: \033[m', contador)




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
                print('En ésta opción se busca por Código de identificación: ')
                cod = int(input('Engrese un código identificador (mayor a cero): '))
                pos = add_in_buscar(vec, cod)
                if pos != - 1:
                    print('\033[1;32m ***Se encontró el Servicio que se buscaba***\033[m')
                    print(vec[pos])
                    if vec[pos].tipo > 4:
                        vec[pos].monto = vec[pos].monto + 100000
                        print(vec[pos])
                else:
                    print('\033[1;31m ---NO Se encontró Ningún Servicio con ese Código Identificador---\033[m')

        elif opcion == 4:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                acumulador_vec(vec)



        elif opcion == 5:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                print('\033[1;35mAquí se solicita un monto, los importes mayores a ellos serán los que se cargarán en el Archivo.\033[m')
                print('\033[1;35mEl monto debe ser con coma flotante.\033[m')

                generar_archivo(archivo, vec)

                if os.path.exists(archivo):
                    print('\033[1;32m***El Archivo se generó con éxito***\033[m')

                else:
                    print('\033[1;32m---Debe cargarlo nuevamente---\033[m')



        elif opcion == 6:
            if not vec:
                print('El arreglo no ha sido cargado todavía debe ir a la opcion 1..')
            else:
                if os.path.exists(archivo):
                    mostrar_archivo(archivo)

                else:
                    print('\033[1;32m---No existe Archivo, debe ir a la opción 5.---\033[m')

        else:
            print('\033[1;36mUsted eligió la opción Salir \n---ADIOS---\033[m')





if __name__ == '__main__':
    principal()
