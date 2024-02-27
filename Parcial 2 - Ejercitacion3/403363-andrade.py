
def leer_archivo(entrada):
    fd= open(entrada,"rt")
    texto = fd.read()
    fd.close()
    return texto

def es_digito(c):
    if c.isdigit():
        return True
    return False

def es_par(cl):
    if int(cl) % 2 == 0:
        return True
    return False

def es_vocal(c):
    car = c.lower()
    vocales = "aeiou"
    if car in vocales:
        return True
    return False

def es_consonante(c):
    car = c.lower()
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    if car in consonantes:
        return True
    return False

def tiene_p(c):
    if c in "pP":
        return True
    return False

def principal():
    r1=r2=r3=r4=0
    texto = leer_archivo("entrada.txt")

    cl = 0
    cant_vocales = 0
    cant_consonantes=0
    tiene_digito = False
    tiene_pP = False
    tiene_mas_de_2 = False
    tiene_una_o_mas_s = False
    cont_palabras = 0
    cont_caracteres = 0
    encontre_r = False
    encontre_ra = False
    hay_vocal_entre_los_dos_primeros = False
    for c in texto:
        if c == " " or c == ".":
            #termino la palabra
            #punto 1
            if es_par(cl) and not tiene_digito:
                if cant_vocales == cant_consonantes:
                    r1 +=1
            #punto 2
            if tiene_digito and not tiene_pP:
                if cl > r2:
                    r2 = cl
            #punto 3
            if tiene_mas_de_2 and tiene_una_o_mas_s:

                cont_palabras += 1
                cont_caracteres+= cl
            #punto 4
            if hay_vocal_entre_los_dos_primeros and encontre_ra:
                r4 += 1
            #apagamos banderas/contadores
            cl = 0
            cant_vocales =0
            cant_consonantes = 0
            tiene_digito = False
            tiene_pP = False
            tiene_mas_de_2 = False
            tiene_una_o_mas_s = False
            encontre_r = False
            encontre_ra = False
            hay_vocal_entre_los_dos_primeros = False
        else:
            cl += 1
            #punto 1
            if es_vocal(c):
                cant_vocales += 1
            if es_consonante(c):
                cant_consonantes += 1
            if es_digito(c):
                tiene_digito = True
            #punto 2
            if tiene_p(c):
                tiene_pP = True

            #punto 3
            if cl > 2:
                tiene_mas_de_2 = True

            if c in "sS":
                tiene_una_o_mas_s = True
            #punto 4

            if c in "Rr":
                encontre_r = True
            else:
                if encontre_r and c in "aA":
                    encontre_ra = True
                else:
                    encontre_r = False

            if cl <= 2 and es_vocal(c):
                hay_vocal_entre_los_dos_primeros = True
    #primedio
    if cont_palabras != 0:
        r3 = cont_caracteres//cont_palabras
    else:
        r3= 0

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    principal()