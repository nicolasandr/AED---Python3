class Servicio:
    def __init__(self, cod, des, cli, tip, mon):
        self.codigo = cod
        self.descripcion = des
        self.cliente = cli
        self.tipo = tip
        self.monto = mon

    def __str__(self):
        cad = 'Codigo: {:<6} | Descripción: {:<20} |  Cliente: {:<20} |  Tipo: {:<2} |  Monto: $ {:<10}'
        return cad.format(self.codigo, self.descripcion, self.cliente, self.tipo, self.monto)
