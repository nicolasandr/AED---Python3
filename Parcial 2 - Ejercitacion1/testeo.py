
def leer_archivo(nombre):
    fd = open(nombre,"rt")
    texto = fd.read()
    fd.close()

    return texto

def es_digito(caracter):
# if "0" <= caracter <= "9": (otra manera de hacerlo)
    if caracter in "0123456789":
        return True
    return False

def es_letra(car):
    car = car.lower()
    if "a" <= car <= "z" or car == "ñ" or car in "áéíóú":
        return True
    return False

def es_letra_minuscula(letra):
    if letra.islower():
        return True
    return False

def es_vocal(car):
    return car.lower() in "aeiouáéíóú"

def principal():

    texto = leer_archivo("entrada.txt")
#variables por palabra
    cl=0
    comienza_digito_impar = True
    todas_minusculas = True
    comienza_vocal= False
    tiene_b= False

    #variables generales
    r1 = r2 = r3 = r4 = 0

    for c in texto:
        if c == " " or c == ".":
        # termino la palabra
        #punto 1
            if comienza_digito_impar and todas_minusculas:
                r1 += 1

        #punto 2
            if tiene_b and comienza_vocal:
                if cl > r2:
                    r2 = cl

        # reiniciar las banderas/contadores por palabra
            cl = 0
            comienza_digito_impar = False
            todas_minusculas = True
            comienza_vocal = False
            tiene_b = False
        else:
            cl += 1
        #punto 1
            if cl == 1 and es_digito(c):
                if int(c) % 2 != 0:
                    comienza_digito_impar = True
                else:
                    if es_digito(c) or not es_letra_minuscula(c):
                        todas_minusculas = False
        #punto 2
            if cl == 1 and es_vocal(c):
                comienza_vocal = True
            if c.lower() == "b":
                tiene_b = True

#calculos de promedio/porcentaje

#impresiones
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    principal()