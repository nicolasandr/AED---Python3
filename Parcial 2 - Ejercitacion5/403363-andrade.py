def leer_archivo(entrada):
    fd = open(entrada,"rt")
    texto = fd.read()
    fd.close()
    return texto

def es_vocal(c):
    car = c.lower()
    vocales = "aeiou"
    if car in vocales:
        return True
    return False

def es_consonante(c):
    car = c.lower()
    consonantes="bcdfghjklmnñpqrstvwxyz"
    if car in consonantes:
        return True
    return False

def es_digito(c):
    if c.isdigit():
        return True
    return False

def tiene_pP(c):
    if c in "pP":
        return True
    return False

def principal():
    r1=r2=r3=r4=0
    texto = leer_archivo("entrada.txt")
   # texto ="Otra rara ocasion para esos tarados."
    cl = 0
    consonantes = 0
    vocales = 0
    cumple_condicion2 = False
    longitud = 0
    cumple_condicion_3 = False
    cantidad_palabras = 0
    cantidad_caracteres = 0
    cr = 0
    encontre_r = False
    encontre_ra = False
    encontre_vocal_al_inicio = False

    for c in texto:
        if c == " " or c == ".":
            #termino la palabra
            #punto1:
            if cl % 2 == 0:
                if vocales == consonantes:
                    r1 += 1
            #punto2
            if cumple_condicion2:
                if longitud > r2:
                    r2 = longitud
            #punto3
            if cumple_condicion_3:
                    cantidad_caracteres += cl
                    cantidad_palabras += 1
            #punto 4
            if encontre_ra and encontre_vocal_al_inicio:
                r4 += 1

            #reseteamos contadores/banderas
            cl = 0
            consonantes = 0
            vocales = 0
            cumple_condicion2 = False
            longitud=0
            cumple_condicion_3 = False
            cumple_condicion4 = False
            encontre_r = False
            encontre_ra = False
            encontre_vocal_al_inicio = False
        else:
            cl += 1
            #resolvemos condicionales
            #punto 1: determinar cantidad
            if not es_digito(c) and es_vocal(c):
                vocales+=1
            if not es_digito(c) and es_consonante(c):
                consonantes+=1
            #punto 2
            if es_digito(c) and not tiene_pP(c):
                cumple_condicion2 = True
                longitud = cl
            #punto 3
            if cl > 2 and c in "sS":
                cumple_condicion_3 = True
            #punto 4
            if c == "r":
                encontre_r = True
            else:
                if encontre_r and c == "a":
                    encontre_ra = True
                else:
                    encontre_r = False

            if es_vocal(c) and cl < 3:
                encontre_vocal_al_inicio = True
    #promedio entero
    if cantidad_palabras != 0:
        r3 = cantidad_caracteres // cantidad_palabras
    else:
        r3 = 0

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__=="__main__":
    principal()