from funciones import *


def menu():
    print('Menu principal:')
    print('seleccione una opcion:')
    print('\n1_Generar articulos:')
    print('2_Mostrar articulos cuyo lugar de origen sean distintos de P')
    print('3_Buscar registro igual al valor cargado por teclado.')
    print('4_Crear archivo de registros.')
    print('Mostrar el archivo creado en el punto anterior.')
    print('Procesar la cadena retornada en el punto 3.')
    print('0_Para finalizar.\n')


def principal():
    entrada = -1
    arreglo_de_registros = []
    file_binary = 'archivo.dat'
    cantidad_articulos = 0
    total_precios = 0
    arreglo_creado = False
    while entrada != 0:
        menu()
        entrada = int(input('ingrese un valor:'))

        if entrada == 1:
            generar_articulos(arreglo_de_registros)
            print('\nSe generaron los articulos correctamente.')
            arreglo_creado = True

        if entrada == 2 and arreglo_creado:
            mostrar_articulos(arreglo_de_registros)

        if entrada == 3 and arreglo_creado:
            indice = buscar_registro(arreglo_de_registros)
            if indice != '\nNo existe\n':
                print(arreglo_de_registros[indice].descripcion)
            else:
                print(indice)

        if entrada == 4 and arreglo_creado:
            cantidad_articulos, total_precios = crear_archivo_binario(file_binary, arreglo_de_registros)
        if entrada == 5:
            mostrar_archivo_binario(file_binary)
            print('cantidad articulos:', cantidad_articulos)
            print('precio de venta prom:', round((total_precios / cantidad_articulos), 2))

        if not arreglo_creado:
            print('\nDebe crear el arreglo! intente nuevamente!.\n')
        if entrada not in (0, 1, 2, 3, 4, 5, 6):
            print('\n Debe ingresar un valor correcto.!\n')


if __name__ == '__main__':
    principal()
