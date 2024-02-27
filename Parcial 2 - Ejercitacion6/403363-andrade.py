
def leer_texto(entrada):
    fd = open(entrada,"rt")
    texto = fd.read()
    fd.close()
    return texto

def es_digito(c):
    if c.isdigit():
        return True
    return False

def es_par(c):
    if int(c) % 2 == 0:
        return True
    return False

def hay_mayusculas(c):
    if c.isupper():
        return True
    return False

def es_vocal(c):
    car = c.lower()
    vocales="aeiou"
    if car in vocales:
        return True
    return False

def es_consonante(c):
    car = c.lower()
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    if car in consonantes:
        return True
    return False

def principal():
    r1=r2=r3=r4=0
    texto = leer_texto("entrada.txt")
    cl=0
    primer_digito_impar = False
    resto_minusculas = True
    comienza_con_vocal = False
    contiene_b = False
    cont_consonantes = 0
    cont_vocales = 0
    contiene_m = False
    contiene_a = False
    cant_caracteres =0
    cant_palabras =0
    tiene_d = False
    ultima = 0
    contiene_vocal = False
    tiene_dd = False

    for c in texto:
        if c == " " or c==".":
            #termino palabra
            #Punto1
            if primer_digito_impar and not resto_minusculas:
                r1 +=1
            #punto 2
            if comienza_con_vocal and contiene_b:
                if cl > r2:
                    r2= cl
            #punto3
            if cont_consonantes > cont_vocales:
                if not contiene_m and not contiene_a:
                    cant_caracteres += cl
                    cant_palabras +=1
            #punto4
            if tiene_dd and contiene_vocal and es_vocal(ultima):
                r4 += 1

            #reiniciamos banderas/contadores
            cl=0
            primer_digito_impar = False
            resto_minusculas = True
            comienza_con_vocal = False
            contiene_b = False
            contiene_m = False
            contiene_a = False
            cont_consonantes =0
            cont_vocales=0
            tiene_d = False
            ultima = 0
            contiene_vocal = False
            tiene_dd = False
        else:
            cl+=1
            #punto1
            if es_digito(c) and cl == 1:
                if not es_par(c):
                    primer_digito_impar = True
            elif hay_mayusculas(c):
                 resto_minusculas = False
            #punto2
            if es_vocal(c) and cl ==1:
                comienza_con_vocal = True
            if c in "bB":
                contiene_b= True
            #punto3:
            if es_consonante(c):
                cont_consonantes += 1
            if es_vocal(c):
                cont_vocales += 1
            if c == "m":
                contiene_m = True
            if c =="a":
                contiene_a = True
            #punto4
            if tiene_d and c == "d":
                tiene_dd = True
            if c == "d":
                tiene_d = True
            if es_vocal(c):
                contiene_vocal = True

            ultima = c

    if cant_palabras !=0:
        r3 = cant_caracteres//cant_palabras
    else:
        r3= 0

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()