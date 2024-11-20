from models.abstract_vehiculo import AbstractVehiculo

class Moto(AbstractVehiculo):
    def __init__(self, matricula, km, casco, valor_alquiler=0.5):
        super().__init__(matricula, km, valor_alquiler=valor_alquiler)
        self.casco = casco

    def calcular_alquiler(self, km):
        return km * self.valor_alquiler

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        casco_info = "Incluye casco" if self.casco else "No incluye casco"
        return f"{datos}, {casco_info}"
