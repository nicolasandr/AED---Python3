from funciones import *


def menu():
    print("Menu principal:")
    print("1. Cargar un arreglo de registros con los datos de n libros.")
    print("2. Mostrar todos los libros del arreglo,")
    print("3. Buscar un vehículo por ISBN. ")
    print(
        "4. A partir del arreglo genere un archivo binario.")
    print("5. Mostrar el archivo generado en el punto anterior indicando, al final, cuántos libros se mostraron.")


def principal():
    entrada = -1
    se_cargo_arreglo = False
    archivo_binario = "archivo.dat"
    while entrada != 0:
        menu()
        entrada = int(input("Ingrese una opcion:"))
        if entrada == 1:
            arreglo_registros = crear_arreglo_registros()
            se_cargo_arreglo = True
        elif entrada == 2 and se_cargo_arreglo:
            mostrar_libros(arreglo_registros)
        elif entrada == 3:
            entrada_isbn = int(input("ingrese ISBN:"))
            indice = buscar_libro(arreglo_registros, entrada_isbn)

            if indice != -1:
                print("datos sin descuento:", arreglo_registros[indice])
                if arreglo_registros[indice].codigo_idioma == 4:
                    porcentaje = 22 * 100 // arreglo_registros[indice].precio_venta
                    arreglo_registros[indice].precio_venta = arreglo_registros[indice].precio_venta - porcentaje
                    print("datos con decuento:", arreglo_registros[indice])
            else:
                print("No se encontro el ISBN")
        elif entrada == 4:
            generar_archivo_binario(arreglo_registros, archivo_binario)
        elif entrada == 5:
            mostrar_archivo_generado(archivo_binario)
        elif entrada not in (0, 1, 2, 3, 4, 5):
            print("Ingrese una opcion valida.")
        elif not se_cargo_arreglo:
            print("Debe cargar el arreglo")

if __name__ == '__main__':
    principal()
