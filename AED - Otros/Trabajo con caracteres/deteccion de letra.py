# encontrar cantidad de "ni" en el file
file = "niniinninn ii"
bandera_i = True
bandera_n = True
cont_ni = 0

for linea in file:

    if linea == "n" and bandera_n:
        bandera_n = False
    elif bandera_n == False and linea == "i":
        cont_ni += 1
        bandera_n = True
    elif bandera_n == False and linea != "i" and linea != "n":
        bandera_n = True

print("cantidad de ni en file:", cont_ni)