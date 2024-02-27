# Funciones utilizadas para la resolución de ejercicios en clase
# V1.0


# --- Funciones de uso general ---


def cargar_mayor_que(valor, mensaje="Ingrese un valor:"):
    num = int(input(mensaje))
    while num <= valor:
        print("Error, debe ingresar un valor mayor que", valor, "!")
        num = int(input(mensaje))
    return num


def cargar_entre(desde, hasta, mensaje="Ingrese un valor:"):
    val = int(input(mensaje))
    while val < desde or val > hasta:
        print("Error, el valor debe estar entre", desde, "y", hasta, "!")
        val = int(input(mensaje))
    return val


# --- Funciones de procesamiento de texto ---


def es_digito(car):
    return car in "0123456789"


def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"


def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


def es_letra(car):
    return es_vocal(car) or es_consonante(car)


def es_mayuscula_v1(car):
    return car in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def es_mayuscula_v2(car):
    return es_letra(car) and car == car.upper()


def validar_texto(tex):
    resultado = True
    if tex is None or len(tex) == 0 or tex[-1] != '.':
        resultado = False
    return resultado


# --- Funciones de procesamiento de arreglos/vectores/listas ---


#  ordena de menor a mayor
def select_sort_asc(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


#  requiere una lista ordenada de menor a mayor
def busqueda_binaria_asc(v, x):
    izq = 0
    der = len(v) - 1
    c = (izq + der) // 2
    while izq <= der and x != v[c]:
        if x > v[c]:
            izq = c + 1
        else:
            der = c - 1
        c = (izq + der) // 2
    if izq > der:
        res = -1
    else:
        res = c
    return res


def busca_mayor(v):
    mayor = None
    for elem in v:
        if mayor is None or elem > mayor:
            mayor = elem
    return mayor


def busca_menor(v):
    menor = None
    for elem in v:
        if menor is None or elem < menor:
            menor = elem
    return menor


def busca_mayor_menor(v):
    mayor = None
    menor = None
    for elem in v:
        if mayor is None or elem > mayor:
            mayor = elem
        if menor is None or elem < menor:
            menor = elem
    return mayor, menor


def sumar_vector(v):
    acum = 0
    for elem in v:
        acum += elem
    return acum


# función de prueba
def prueba():
    print(es_digito('9'))
    print(es_vocal('a'))
    print(es_consonante('b'))
    print(es_letra('w'))
    print(es_mayuscula_v1('T'))
    print(es_mayuscula_v2('T'))


# script principal
if __name__ == '__main__':
    prueba()
