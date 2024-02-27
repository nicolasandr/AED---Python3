class Paquete:
    def __init__(self, id, titulo, transporte, monto, destino, cliente):
        self.id = id
        self.titulo = titulo
        self.transporte = transporte
        self.monto = monto
        self.destino = destino
        self.cliente = cliente

    def __str__(self):
        r = 'id:' + str(self.id) + '\t' + 'titulo:' + str(self.titulo) + '\t' + 'transporte:' + str(
            self.transporte) + '\t' + 'monto:' + str(self.monto) + '\t' + 'destino:' + str(
            self.destino) + '\t' + 'cliente:' + str(self.cliente)
        return r
