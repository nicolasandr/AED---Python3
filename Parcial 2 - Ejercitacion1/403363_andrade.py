def leer_archivo(archivo):
    fd = open(archivo,"rt")
    texto = fd.read()
    fd.close()
    return texto

def es_digito(car):
    if car.isdigit():
        return True
    return False

def es_letra_minuscula(car):
    if car.islower():
        return True
    return False

def es_vocal(car):
    if car in "aeiuo":
        return True
    return False

def es_consonante(car):
    if car in "bcdfghjklmnñpqrstvwxyz":
        return True
    return False

def principal():
    r1=r2=r3=r4=0
    texto = leer_archivo("entrada.txt")
    cl = 0
    primera_es_impar = False
    todas_minusculas = True
    primera_es_vocal = False
    contiene_bB = False
    cant_vocales_por_palabra=0
    cant_consonantes_por_palabra=0
    no_tiene_ma = True
    cantidad_palabras = 0
    cantidad_letras =0
    tiene_dos_d = False
    contiene_d = False
    car_ant = 0

    for car in texto:
        if car == " " or car == ".":
            #fin de palabra
            if primera_es_impar and todas_minusculas:
                r1 += 1
            #Punto 2
            if primera_es_vocal and contiene_bB:
                if cl > r2:
                    r2 = cl
            #Punto 3
            if no_tiene_ma:
                if cant_consonantes_por_palabra > cant_vocales_por_palabra:
                    cantidad_palabras += 1
                    cantidad_letras += cl
            #Punto 4
            if tiene_dos_d and es_vocal(car_ant):
                r4 += 1
            #reiniciar contadores/banderas
            cl = 0
            primera_es_impar = False
            todas_minusculas = True
            primera_es_vocal = False
            contiene_bB = False
            cant_vocales_por_palabra = 0
            cant_consonantes_por_palabra = 0
            no_tiene_ma=True
            tiene_dos_d = False
            contiene_d = False
            car_ant = 0
        else:
            cl +=1
            #punto 1
            if es_digito(car) and cl == 1:
                if int(car)%2 != 0:
                    primera_es_impar= True
            else:
                if es_digito(car) or not es_letra_minuscula(car):
                    todas_minusculas = False
            #punto 2
            if es_vocal(car) and cl == 1:
                primera_es_vocal = True
            if car in "bB":
                contiene_bB = True
            #punto 3
            if es_vocal(car):
                cant_vocales_por_palabra +=1
            if es_consonante(car):
                cant_consonantes_por_palabra += 1
            if car in "ma":
                no_tiene_ma = False
            #punto 4
            if contiene_d and car =="d":
                tiene_dos_d = True
            if car =="d":
                contiene_d = True

            car_ant = car
        #promedio entero
    r3 = cantidad_letras//cantidad_palabras

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__=="__main__":
    principal()