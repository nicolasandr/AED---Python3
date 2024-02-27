import pickle
import os

from soporte import *


def main():
    print('\n')
    print('-' * 100)
    print('Menu principal:\n')
    print('0_para finalizar.')
    print('1_Generar un arreglo de n tickets.')
    print('2_mostrar los datos del arreglo.')
    print('3_buscar codigo y modificar monto si este existe.')
    print('4_Determinar la cantidad de tickets vendidos')
    print('5_grabar los datos en archivo binario.')
    print('6_Mostrar el archivo generado anteriormente.')
    print('-' * 100)


def mostrar_tickets(arreglo):
    for i in arreglo:
        print(i)


def buscar_codigo_vuelo(arreglo, id):
    izq, der = 0, len(arreglo) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if int(id) == int(arreglo[medio].id):
            return medio
        elif int(id) < int(arreglo[medio].id):
            der = medio - 1
        else:
            izq = medio + 1
    return -1


def cant_tickets_por_asiento_y_clase(arreglo):
    # columna:asiento        fila:clase
    mat_cant_tickets = [[0] * 140 for _ in range(10)]
    for p in arreglo:
        mat_cant_tickets[p.clase][p.asiento] += 1

    for i in range(len(mat_cant_tickets)):
        for j in range(len(mat_cant_tickets[0])):
            if mat_cant_tickets[i][j] != 0:
                print('para el asiento:', j, 'y la clase:', i, 'hay vendidos:', mat_cant_tickets[i][j], 'tickets')


def crear_archivo_binario(arreglo_registros, archivo):
    file_binary = open(archivo, 'wb')
    aer1 = input('\nIngrese aeropuerto origen:')
    aer2 = input('\nIngrese aeropuerto destino:')
    for ticket in arreglo_registros:
        if aer1 == ticket.origen and aer2 == ticket.destino and ticket.clase not in (0, 1):
            pickle.dump(ticket, file_binary)
    file_binary.close()


def mostrar_archivo_binario(archivo):
    cont = 0
    monto_total_tickets = 0
    if not os.path.exists(archivo):
        print('\nEl archivo:', archivo, 'no existe.')
    else:
        file_binary = open(archivo, 'rb')
        while file_binary.tell() < os.path.getsize(archivo):
            ticket = pickle.load(file_binary)
            print(ticket)
            monto_total_tickets += ticket.monto
            cont += 1
        file_binary.close()

    if cont == 0:
        print('\nNo existen tickets para calcular el promedio del monto')
    else:
        promedio = monto_total_tickets // cont
        print('\ncantidad de registros mostrados:', cont)
        print('\nmonto promedio pagado de los tickets mostrados:', promedio)


def principal():
    tickets_generados = False
    entrada = -1
    archivo = 'tickets.dat'
    while entrada != 0:
        main()
        entrada = int(input('\nIngese una opcion:'))
        if entrada == 1:
            arreglo_registros = generar_ticket()
            if arreglo_registros is None:
                print('\nNo se pudo cargar el arreglo')
            else:
                print('\nSe generaron los registros')
                tickets_generados = True
        elif entrada == 2 and tickets_generados:
            mostrar_tickets(arreglo_registros)
        elif entrada == 3 and tickets_generados:
            codigo = int(input('\nIngrese codigo de vuelo:'))
            indice = buscar_codigo_vuelo(arreglo_registros, codigo)
            if indice == -1:
                print('\nno existe el codigo buscado.')
            else:
                porcentaje = (10 * arreglo_registros[indice].monto) // 100
                arreglo_registros[indice].monto = arreglo_registros[indice].monto + porcentaje
                print('\nse modifico el monto en el ticket:', arreglo_registros[indice].monto)
        elif entrada == 4 and tickets_generados:
            cant_tickets_por_asiento_y_clase(arreglo_registros)
        elif entrada == 5 and tickets_generados:
            crear_archivo_binario(arreglo_registros, archivo)
        elif entrada == 6:
            mostrar_archivo_binario(archivo)
        elif entrada not in (0, 1, 2, 3, 4, 5, 6):
            print('\ningrese un numero del menu.')
        elif not tickets_generados:
            print('\nPrimero debe cargar el arreglo!')


if __name__ == '__main__':
    principal()
