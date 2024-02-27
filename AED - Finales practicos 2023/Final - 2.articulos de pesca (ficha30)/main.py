import random
from funciones import Paquete


def menu():
    print('\nMenu de opciones:')
    print("1_Generar un arreglo.")
    print("2_Mostrar los datos del arreglo")
    print('3_Buscar por titulo')
    print('\n0_ para finalizar')


def add_in_order(paquete, arreglo):
    izq, der, pos = 0, len(arreglo) - 1, 0
    while izq <= der:
        c = (izq + der) // 2
        if paquete.id == arreglo[c].id:
            pos = c
            break
        elif paquete.id <= arreglo[c].id:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
        arreglo[pos:pos] = [paquete]


def generar_arreglo(arreglo):
    n = int(input('ingrese la cantidad de registros que desea generar:'))

    for i in range(n):
        paquetes = ['paquete1', 'paquete2', 'paquete3']
        nombre = ['nicolas', 'lucas', 'lucia']
        apellido = ['juarez', 'martinez', 'andrade']
        id = random.randint(1, 100)
        titulo = random.choice(paquetes)
        transporte = random.randint(0, 9)
        monto = random.uniform(10, 100)
        destino = random.randint(1, 50)
        nombre = nombre[random.randint(0, 2)] + str('\t') + apellido[random.randint(0, 2)]

        paquete = Paquete(id, titulo, transporte, monto, destino, nombre)
        add_in_order(paquete, arreglo)

    print('\nse mostraron:', n, 'registros.\n')


def mostrar_arreglo(arreglo):
    for i in arreglo:
        print(i)


def buscar_tit(tit, arreglo_registros):
    for i in range(len(arreglo_registros)):
        if tit == arreglo_registros[i].titulo:
            print('id:', arreglo_registros[i].id, '\nnombre cliente:', arreglo_registros[i].nom_cliente)
            return 0
    return -1


def principal():
    entrada = -1
    arreglo_registros = []
    arreglo_generado = False

    while entrada != 0:
        menu()
        entrada = int(input('\nIngrese una opcion:'))
        if entrada == 1:
            generar_arreglo(arreglo_registros)
            arreglo_generado = True
        elif entrada == 2 and arreglo_generado:
            mostrar_arreglo(arreglo_registros)
        elif entrada == 3 and arreglo_generado:
            tit = input('\nIngrese el titulo que desea buscar:')
            indice = buscar_tit(tit, arreglo_registros)
            if indice == -1:
                print('No se encontro el titulo')
        elif entrada not in (0, 1, 2, 3, 4):
            print('Debe ingrersar una opcion correcta!\n')


if __name__ == '__main__':
    principal()
