class Deportista:
    def __init__(self, id, nombre, tipo_deporte, tipo_beca, monto_beca):
        self.id = id
        self.nombre = nombre
        self.tipo_deporte = tipo_deporte
        self.tipo_beca = tipo_beca
        self.monto_beca = monto_beca

    def __str__(self):
        r = 'id:' + str(self.id) + '\t' + 'nombre:' + str(self.nombre) + '\t' + 'tipo_deporte:' + str(
            self.tipo_deporte) + '\t' + 'tipo_beca:' + str(self.tipo_beca) + '\t' + 'monto_beca:' + str(self.monto_beca)
        return r
