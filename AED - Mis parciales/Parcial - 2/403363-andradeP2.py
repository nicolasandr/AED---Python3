def leer_archivo(entrada):
    fd = open(entrada,"rt")
    texto = fd.read()
    fd.close()
    return texto

def es_consonante(c):
    car = c.lower()
    consonantes="bcdfghjklmnpqrstvwxyz"

    if car in consonantes:
        return True
    return False

def es_digito(c):
    if c.isdigit():
        return True
    return False

def es_vocal(c):
    car = c.lower()
    vocales="aeiou"
    if car in vocales:
        return True
    return False

def Principal():
    r1=r2=r3=r4=0
    texto = leer_archivo("entrada.txt")
    cl=0
    cant_consonantes=0
    digito_en_2_3 = False
    tiene_vocal = False
    ultimo = 0
    cant_palabras = 0
    cont_palabra = 0
    tiene_vocal_p1 = False
    tiene_vocal_p2 = False
    tiene_vocal_p3 = False
    tiene_4_o_mas_caracteres = False
    encontre_d = False
    encontre_de = False
    encontre_t_despues_de_de = False

    for c in texto:
        if c==" " or c==".":
            #termina palabra
            cont_palabra +=1
            #punto 1
            if digito_en_2_3 and cant_consonantes >= 2:
                r1 += 1
            #punto2
            if tiene_vocal and es_digito(ultimo):
                cant_palabras += 1
            #punto3
            if tiene_4_o_mas_caracteres and tiene_vocal_p1 and tiene_vocal_p2 and tiene_vocal_p3:
                r3 +=1
            #punto4
            if encontre_t_despues_de_de:
                r4+=1
            #reiniciamos banderas/contadores
            cl=0
            cant_consonantes =0
            digito_en_2_3 = False
            tiene_vocal = False
            ultimo = 0
            tiene_vocal_p1 = False
            tiene_vocal_p2 = False
            tiene_vocal_p3 = False
            tiene_4_o_mas_caracteres=False
            encontre_d = False
            encontre_de = False
            encontre_t_despues_de_de = False

        else:
            cl+=1
            #punto1
            if cl >= 4:
                if es_consonante(c):
                    cant_consonantes +=1

            if es_digito(c) and cl == 2:
                digito_en_2_3=True
            if es_digito(c) and cl ==3:
                digito_en_2_3=True
            #Punto2
            if es_vocal(c):
                tiene_vocal = True
            ultimo= c
            #punto3
            if es_vocal(c) and cl==1:
                tiene_vocal_p1= True
            if es_vocal(c) and cl == 2:
                tiene_vocal_p2 = True
            if es_vocal(c) and cl == 3:
                tiene_vocal_p3 = True
            if cl >=4:
                tiene_4_o_mas_caracteres=True
            #punto4
            if c in "dD":
                encontre_d =True
            else:
                if encontre_d and c in "eE":
                    encontre_de= True
                else:
                    encontre_d=False

            if encontre_de and c in "tT":
                encontre_t_despues_de_de =True
    #porcentaje entero
    if cont_palabra !=0:
        r2 = cant_palabras * 100 // cont_palabra
    else:
        r2 = 0

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    Principal()