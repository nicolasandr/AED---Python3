import os.path
import pickle
import random


class Entrada:
    def __init__(self, numero, nombre_pelicula, tipo_proyeccion, clasificacion, precio_entrada, dia_de_venta):
        self.numero = numero
        self.nombre_pelicula = nombre_pelicula
        self.tipo_proyeccion = tipo_proyeccion
        self.clasificacion = clasificacion
        self.precio_entrada = precio_entrada
        self.dia_de_venta = dia_de_venta

    def __str__(self):
        tipo = ['Normal', '3D', 'IMAX', 'IMAX 3D']
        clasif = ['ATP', 'M13', 'M16', 'M18']
        return (
            f'| numero:{self.numero:<10} | pelicula{self.nombre_pelicula:<60} | tipo:{tipo[self.tipo_proyeccion - 1]:>4} | Clasificacion:{clasif[self.clasificacion]:>4} | '
            f'precio:{self.precio_entrada:>10.2f} | dia de venta:{self.dia_de_venta:>3} |\n {"-" * 109}')


def se_creo_arch_bin(fb):
    if os.path.exists(fb):
        return True
    return False


def archivo(fb='tickets.dat'):
    cant_entradas_vendidas = 20
    nombres = ['ted', 'nija', 'la monja', 'El sobreviviente']
    file_binary = open(fb, 'wb')
    for _ in range(cant_entradas_vendidas):
        numero = random.randint(1, 999)
        nombre_pelicula = random.choice(nombres)
        tipo_proyeccion = random.randint(1, 4)
        clasificacion = random.randint(0, 3)
        precio_entrada = random.randint(1000, 20000)
        dia_de_venta = random.randint(1, 31)

        entrada = Entrada(numero, nombre_pelicula, tipo_proyeccion, clasificacion, precio_entrada, dia_de_venta)
        pickle.dump(entrada, file_binary)

    file_binary.close()

    if se_creo_arch_bin(fb):
        print('\nArchivo binario cargado con exito')
    else:
        print('\nNo se creo el archivo binario')


if __name__ == '__main__':
    archivo()
