class Trabajo:
    def __init__(self, id, nombre, tipo, importe, cantidad_de_personal):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe
        self.cantidad_de_personal = cantidad_de_personal

    def __str__(self):
        r = "id:"+str(self.id) + " " + "nombre:"+str(self.nombre) + " " + "tipo:"+str(self.tipo) + " " +"importe:"+ str(self.importe) + " " +"cantidad de personal:"+ str(
            self.cantidad_de_personal) + " "

        return r


def menu():
    print("\nMenu principal:")
    print("1_ cargar arreglo con los datos de trabajo")
    print("2_ mostrar todos los datos de todos los trabajos de mayo a menor segun los importes a cobrar")
    print("3_ determinar y mostrar datos con mayor cantidad de personal afectado ")
    print("4_ determinar si existe trabajo cuya descripcion sea igual al valor que carga por teclado.()\n")


"""
datos:
id
nombre del trabajo
tipo de trabajo (un valor de 0 a 3, 0: interior, 1: exterior, 2: piletas, 3: tapizados)
importe a cobrar por ese trabajo
la cantidad de personal afectado para prestar ese servicio. 

n= define tamaño de registros
"""
