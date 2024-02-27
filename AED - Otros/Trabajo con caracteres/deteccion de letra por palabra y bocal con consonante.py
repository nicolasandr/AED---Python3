# encontrar cantidad de "ni" en el file. (Aclaracion: si se encontro mas de un 'ni' por palabra solo contemplar uno)
# agregado: detectar cuantas palabras tienen una bocal al inicio y una consonante al final.

file = "respeten los colores respeten a la inchada "
bandera_n = True
bandera_espacio = True
deteccion_espacio = True
cont_ni = cont_vocales = 0
vocal = "aeiou"

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
        deteccion_espacio = True

    for letra in vocal:
        print(linea, ":", letra , ":", deteccion_espacio)
        if linea == letra and deteccion_espacio:
         #   print(linea, ":", letra)
            cont_vocales += 1

    if linea != " ":
        deteccion_espacio = False

print("cantidad de ni en file:", cont_ni)
print("contador de la cantidad de palabras que inician con una vocal:", cont_vocales)