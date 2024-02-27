class Paquete:
    def __init__(self, id, titulo, transporte, monto, destino, nom_cliente):
        self.id = id
        self.titulo = titulo
        self.transporte = transporte
        self.monto = monto
        self.destino = destino
        self.nom_cliente = nom_cliente

    def __str__(self):
        r = 'id:' + str(self.id) + '\t' + 'titulo:' + str(self.titulo) + '\t' + 'transporte:' + str(self.transporte) + '\t' + 'monto:' + str(self.monto) + '\t' + 'destino:' + str(self.destino) + '\t' + 'Nombre:' + str(self.nom_cliente)
        return r
