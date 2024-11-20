from models.abstract_vehiculo import AbstractVehiculo

class Furgoneta(AbstractVehiculo):
    def __init__(self, matricula, km, capacidad, valor_alquiler=1.5):
        super().__init__(matricula, km, valor_alquiler=valor_alquiler)
        self.capacidad = capacidad

    def calcular_alquiler(self, km):
        return km * self.valor_alquiler

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        return f"{datos}, Capacidad: {self.capacidad} m³"
