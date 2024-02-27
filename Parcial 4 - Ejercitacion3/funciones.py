import os.path
import pickle
import random


class Articulo:
    def __init__(self, id, descripcion, precio, lugar, tipo):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.lugar = lugar
        self.tipo = tipo

    def __str__(self):
        pais = ['Argentina', 'Brasil']
        articulo = ['anzuelo', 'caña']
        r = 'id:' + str(self.id) + '\t' + 'descripcion:' + str(self.descripcion) + '\t' + 'precio:' + str(
            self.precio) + '\t' + 'lugar:' + str(pais[self.lugar]) + '\t' + 'tipo:' + str(articulo[self.tipo]) + '\t'
        return r


def add_in_order(articulo, arreglo_registros):
    izq, der, pos = 0, len(arreglo_registros) - 1, 0
    while izq < der:
        medio = (izq + der) // 2
        if articulo.id == arreglo_registros[medio].id:
            pos = medio
            break
        elif articulo.id <= arreglo_registros[medio].id:
            der = medio - 1
        else:
            izq = medio + 1
    if izq > der:
        pos = izq
    arreglo_registros[pos:pos] = [articulo]


def generar_articulos(arreglo_de_registros):
    articulo = ['caña', 'boya', 'anzuelo', 'reel', 'tanza']
    adjetivo = ['grande', 'verde', 'azul', 'naranja', 'metalic', 'elastic']
    cantidad = int(input('\nIngrese la cantidad de articulos que desea generar:'))

    for _ in range(cantidad):
        id = random.randint(100, 999)
        descripcion = random.choice(articulo) + ' ' + random.choice(adjetivo) + '.'
        precio = random.randint(2000, 10000)
        lugar = random.randint(0, 1)
        tipo = random.randint(0, 1)
        objeto = Articulo(id, descripcion, precio, lugar, tipo)
        add_in_order(objeto, arreglo_de_registros)


def mostrar_articulos(arreglo_de_registros):
    entrada = int(input('\nIngrese lugar de origen(0:arg, 1:Br):'))
    for i in arreglo_de_registros:
        if entrada != i.lugar:
            print(i)


def buscar_registro(arreglo_de_registros):
    num = int(input('Ingrese id que desea buscar:'))
    izq, der = 0, len(arreglo_de_registros) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if num == arreglo_de_registros[medio].id:
            return medio
        elif num < arreglo_de_registros[medio].id:
            der = medio - 1
        else:
            izq = medio + 1
    return 'No existe'


def crear_archivo_binario(arch_bin, arreglo_registros):
    cantidad_articulos = 0
    total_precios = 0
    tipo = int(input('\nIngrese tipo de vehiculo (0:argentina, 1:brasil:)'))
    file_binary = open(arch_bin, 'wb')
    for articulo in arreglo_registros:
        if tipo != articulo.tipo:
            pickle.dump(articulo, file_binary)
            cantidad_articulos += 1
            total_precios += articulo.precio
    file_binary.close()
    print('\nEl archivo binario fue reado con exito!.\n')

    return cantidad_articulos, total_precios


def mostrar_archivo_binario(arch_bin):

    if not os.path.exists(arch_bin):
        print('no se encontro el archivo con el nombre:', arch_bin)
    else:
        file_binary = open(arch_bin, 'rb')
        while file_binary.tell() < os.path.getsize(arch_bin):
            print(pickle.load(file_binary))
        file_binary.close()