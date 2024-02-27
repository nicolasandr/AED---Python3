def leerArchivo(nombre_archivo):
    archivo = open(nombre_archivo,"rt")
    contenido = archivo.read()
    archivo.close()
    return contenido

texto = leerArchivo('texto.txt').lower()
print(texto)