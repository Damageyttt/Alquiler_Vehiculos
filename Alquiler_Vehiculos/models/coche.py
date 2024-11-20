from models.abstract_vehiculo import AbstractVehiculo

class Coche(AbstractVehiculo):
    def __init__(self, matricula, km, extras, valor_alquiler=1.0):
        super().__init__(matricula, km, valor_alquiler=valor_alquiler)
        self.extras = extras

    def calcular_alquiler(self, km):
        "Según los kilometros recorridos será el valor del alquiler."
        return km * self.valor_alquiler

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        extras_info = "Incluye extras" if self.extras else "No incluye extras"
        return f"{datos}, {extras_info}"

