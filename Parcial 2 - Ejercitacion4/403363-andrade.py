def leer_archivo(entrada):

    fd= open(entrada,"rt")
    texto = fd.read()
    fd.close()
    return texto

def es_digito(c):
    if c.isdigit():
        return True
    return False

def es_impar(c):
    if int(c) % 2 != 0:
        return True
    return False

def letras_minusculas(c):
    if c.islower():
        return True
    return False
def es_vocal(c):
    vocales = "aeiou"
    if c in vocales:
        return True
    return False

def es_consonante(c):
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    if c in consonantes:
        return True
    return False

def Principal():

    r1=r2=r3=r4=0
    texto = leer_archivo("entrada.txt")
    cl = 0
    resto_es_minuscula = False
    primera_es_digito_impar = False
    contiene_vocal = False
    contiene_bB = False
    cant_consonantes =0
    cant_vocales =0
    contiene_m = False
    contiene_a = False
    cant_palabras=0
    cant_letras =0
    contiene_d = False
    contiene_d_d  = False
    ultima_letra =0
    tiene_una_vocal = False

    for c in texto:
        if c == " " or c == ".":
            #fin palabra
            #punto 1
            if primera_es_digito_impar and resto_es_minuscula:
                r1 += 1
            #punto2
            if contiene_vocal and contiene_bB:
                if cl > r2:
                    r2 = cl
            #punto3:
            if not contiene_m and not contiene_a:
                if cant_consonantes > cant_vocales:
                    cant_palabras += 1
                    cant_letras += cl
            #Punto4
            if contiene_d_d and es_vocal(ultima_letra) and tiene_una_vocal:
                r4 += 1
            #reiniciamos banderas/contadores
            cl = 0
            primera_es_digito_impar = False
            resto_es_minuscula = False
            contiene_vocal = False
            contiene_bB = False
            cant_consonantes = 0
            cant_vocales = 0
            contiene_m = False
            contiene_a = False
            contiene_d = False
            contiene_d_d  = False
            ultima_letra = 0
            tiene_una_vocal = False

        else:
            cl +=1
            #procesamos palabra
            #Punto 1
            if es_digito(c) and cl == 1:
                if es_impar(c):
                    primera_es_digito_impar = True
            else:
                if letras_minusculas(c):
                    resto_es_minuscula = True
                else:
                    resto_es_minuscula = False
            #punto2
            if es_vocal(c):
                contiene_vocal = True
            if c in "bB":
                contiene_bB = True
            #punto3
            if es_consonante(c):
                cant_consonantes +=1
            if es_vocal(c):
                cant_vocales +=1
            if c in "mM":
                contiene_m = True
            if c in "aA":
                contiene_a = True
            #punto4
            #if contiene_d and c =="d":
            #    contiene_d_d = True
            if contiene_d and c=="d":
                contiene_d_d = True
            if c =="d":
                contiene_d = True

            if es_vocal(c):
                tiene_una_vocal = True

            ultima_letra = c

    #promedio
    if cant_palabras != 0:
        r3 = cant_letras//cant_palabras
    else:
        r3 =0

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__=="__main__":
    Principal()