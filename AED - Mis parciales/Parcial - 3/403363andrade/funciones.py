import os.path
import pickle
import random


class Libro:
    def __init__(self, isbn, titulo, autor, codigo_idioma, precio_venta):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.codigo_idioma = codigo_idioma
        self.precio_venta = precio_venta

    def __str__(self):
        idioma = ["Español", "Ingles", "Portugues", "Frances", "Italiano"]
        r = "ISBN:" + str(self.isbn) + "\ttitulo:" + str(self.titulo) + "\tautor:" + str(
            self.autor) + "\tcodigo de idioma:" + str(idioma[self.codigo_idioma - 1]) + "\tprecio de venta:" + str(
            self.precio_venta)
        return r


def add_in_order(arreglo_registros, libro):
    izq, der, pos = 0, len(arreglo_registros) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        if libro.isbn == arreglo_registros[medio].isbn:
            pos = medio
            break
        elif libro.isbn <= arreglo_registros[medio].isbn:
            der = medio - 1
        else:
            izq = medio + 1

    if izq > der:
        pos = izq
    arreglo_registros[pos:pos] = [libro]


def crear_arreglo_registros():
    arreglo_registros = []
    n = int(input("Ingrese la cantidad de libros que desea generar:"))
    titulos = ["titulo1", "titulo2", "titulo3"]
    autores = ["autor1", "autor2", "autor3"]
    for _ in range(n):
        isbn = random.randint(1111111111111, 2222222222222)
        titulo = random.choice(titulos)
        autor = random.choice(autores)
        codigo_idioma = random.randint(1, 5)
        precio_venta = random.randint(100, 434)

        libro = Libro(isbn, titulo, autor, codigo_idioma, precio_venta)

        add_in_order(arreglo_registros, libro)

    return arreglo_registros


def mostrar_libros(arreglo_registros):
    for linea in arreglo_registros:
        print(linea)


def buscar_libro(arreglo_registros, entrada_isbn):
    izq, der = 0, len(arreglo_registros) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if entrada_isbn == arreglo_registros[medio].isbn:
            return medio
        elif entrada_isbn < arreglo_registros[medio].isbn:
            der = medio - 1
        else:
            izq = medio + 1
    return -1


def generar_archivo_binario(arreglo_registros, arch_bin):
    autor = input("\ningrese auntor:")
    precio = int(input("Ingrese precio:"))

    file_binary = open(arch_bin, "wb")
    for libro in arreglo_registros:
        if libro.autor == autor and (libro.precio_venta  < precio):
            pickle.dump(libro, file_binary)
    file_binary.close()


def mostrar_archivo_generado(arch_bin):
    file_binary = open(arch_bin, "rb")
    cont = 0
    if not os.path.exists(arch_bin):
        print("No se encontro el archivo con nombre", arch_bin)
        return

    while file_binary.tell() < os.path.getsize(arch_bin):
        print(pickle.load(file_binary))
        cont += 1
    print("Se mostraron", cont, "libros.")
