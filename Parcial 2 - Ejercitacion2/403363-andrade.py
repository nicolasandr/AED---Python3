def leer_texto(entrada):
    fd = open(entrada, "rt")
    texto = fd.read()
    fd.close()
    return texto

def es_consonante(c):
    car = c.lower()
    consonantes= "bcdfghjklmnñpqrstvwxyz"
    if car in consonantes:
        return True
    return False

def es_vocal(c):
    car = c.lower()
    vocales = "aeiou"
    if car in vocales:
        return True
    return False

def es_digito(c):
    if c.isdigit():
        return True
    return False

def long_es_impar(cl):
    if int(cl) % 2 != 0:
        return True
    return False

def Principal():
    r1=r2=r3=r4=0
    texto = leer_texto("entrada.txt")
    cl = 0
    contiene_consonante_3_5 = False
    ultima = 0
    contiene_digito=False
    tamanio = 0
    encontre_t = False
    encontre_t_s = False
    cant_caracteres = 0
    cant_palabras = 0
    encontre_m = False
    encontre_m_a = False
    primera_letra_texto = 0
    hay_ma_a_partir_de_4 = False
    contiene_primer_letra_texto = False
    cont_sin_reset =0
    for c in texto:
        if c ==" " or c==".":
            #termina palabra
            #punto 1
            if contiene_consonante_3_5 and es_vocal(ultima):
                r1+=1
            #punto2
            if contiene_digito and long_es_impar(tamanio):
                r2+=1
            #punto3
            if encontre_t_s:
                cant_caracteres += cl
                cant_palabras +=1
            #punto4
            if hay_ma_a_partir_de_4 and contiene_primer_letra_texto:
                r4+=1
            #reiniciamos contadores/banderas
            cl = 0
            contiene_consonante_3_5 = False
            ultima = 0
            contiene_digito = False
            tamanio = 0
            encontre_t = False
            encontre_t_s = False
            encontre_m = False
            hay_ma_a_partir_de_4 = False
            contiene_primer_letra_texto = False
        else:
            cl += 1
            tamanio+=1
            cont_sin_reset+=1
            #punto 1
            if es_consonante(c) and cl == 3:
                contiene_consonante_3_5 = True
            if es_consonante(c) and cl == 5:
                contiene_consonante_3_5 = True
            ultima = c
            #punto2
            if es_digito(c):
                contiene_digito= True
            #punto3
            if c in "tT":
                encontre_t = True

            if encontre_t and c in "sS":
                encontre_t_s=True

            #punto4
            if cl >= 4:
                if c in "m":
                    encontre_m = True
                else:
                    if encontre_m and c in "a":
                        hay_ma_a_partir_de_4 = True
                    else:
                        encontre_m = False

            if cont_sin_reset == 1:
                primera_letra_texto = c

            if primera_letra_texto == c:
                contiene_primer_letra_texto=True

    #promedio entero
    if cant_palabras !=0:
        r3 = cant_caracteres//cant_palabras
    else:
        r3=0

    print("valor1:",r1)
    print("valor2:", r2)
    print("valor3:", r3)
    print("valor4:", r4)

if __name__ == '__main__':
    Principal()