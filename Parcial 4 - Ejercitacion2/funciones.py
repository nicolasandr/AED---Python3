class Consumo:
    def __init__(self, num_telefono, hora_de_consumo, tipo_consumo, monto_consumo):
        self.num_telefono = num_telefono
        self.hora_de_consumo = hora_de_consumo
        self.tipo_consumo = tipo_consumo
        self.monto_consumo = monto_consumo

    def __str__(self):
        consumo = ["SMS", "Llamada", "Uso de datos"]
        r = "num_telefono:" + str(self.num_telefono) + "\thora_de_consumo:" + str(
            self.hora_de_consumo) + "\ttipo_consumo:" + str(consumo[(self.tipo_consumo)-1]) + "\tmonto_consumo:" + str(
            self.monto_consumo)
        return r
