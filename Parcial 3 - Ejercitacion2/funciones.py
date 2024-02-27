class Concursante:
    def __init__(self,dni,nombre,cargo,puntaje):
        self.dni = dni
        self.nombre = nombre
        self.cargo = cargo
        self.puntaje = puntaje

    def __str__(self):
        r = "dni:"+str(self.dni)+"\nnombre:"+str(self.nombre)+"\ncargo:"+str(self.cargo)+"\npuntaje:"+str(self.puntaje)+"\n"
        return r


def menu():
    print("Menu principal")
    print("opcion 1")
    print("opcion 2")
    print("salir: 0")
