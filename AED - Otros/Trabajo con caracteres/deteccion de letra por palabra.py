# encontrar cantidad de "ni" en el file. (Aclaracion: si se encontro mas de un 'ni' por palabra solo contemplar uno)
file = "  ninininicolas ni nsn sii anidrade"
bandera_n = True
bandera_espacio = True
cont_ni = 0

for linea in file:

    if linea == "n" and bandera_n:
        bandera_n = False

    elif bandera_n == False and linea == "i" and bandera_espacio:
        cont_ni += 1
        bandera_n = True
        bandera_espacio = False

    elif bandera_n == False and linea != "i" and linea != "n":
        bandera_n = True

    if linea == " ":
        bandera_espacio = True

print("cantidad de ni en file:", cont_ni)