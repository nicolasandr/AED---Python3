import random


class Ticket:
    def __init__(self, id, pasajero, asiento, clase, origen, destino, monto):
        self.id = id
        self.pasajero = pasajero
        self.asiento = asiento
        self.clase = clase
        self.origen = origen
        self.destino = destino
        self.monto = monto

    def __str__(self):
        r = 'id:' + self.id + '\t' + 'pasajero:' + str(self.pasajero) + '\t''asiento:' + str(
            self.asiento) + '\t''clase:' + str(self.clase) + '\t''origen:' + str(self.origen) + '\t''destino:' + str(
            self.destino) + '\t''monto:' + str(self.monto) + '\t'
        return r


def add_in_order(ticket, v):
    izq, der, pos = 0, len(v) - 1, 0
    while izq <= der:
        medio = (izq + der) // 2
        if int(ticket.id) == int(v[medio].id):
            pos = medio
            break
        elif int(ticket.id) <= int(v[medio].id):
            der = medio - 1
        else:
            izq = medio + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [ticket]


def generar_ticket():
    arreglo_registros = []
    nombre = ('nicolas', 'lucas', 'marcos')
    apellido = ('martinez', 'perez', 'ortega')
    origenes = ('jujuy', 'cordoba', 'salta', 'buenos aires')
    destinos = ('tucuman', 'la rioja', 'san juan', 'san luis')

    entrada = int(input('\ningrese la cantidad de tikets que desea generar:'))
    for _ in range(entrada):
        id = str(random.randint(100, 999))
        pasajero = random.choice(nombre) + ' ' + random.choice(apellido)
        asiento = random.randint(1, 140)
        clase = random.randint(0, 9)
        origen = random.choice(origenes)
        destino = random.choice(destinos)
        monto = round(random.uniform(1000, 2000), 2)

        ticket = Ticket(id, pasajero, asiento, clase, origen, destino, monto)
        add_in_order(ticket, arreglo_registros)
    return arreglo_registros

