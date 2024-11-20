from abc import ABC, abstractmethod

class AbstractVehiculo(ABC):
    def __init__(self, matricula, km, estado=True, valor_alquiler=0.0):
        self.matricula = matricula
        self.km = km
        self.estado = estado
        self.valor_alquiler = valor_alquiler

    @abstractmethod
    def calcular_alquiler(self, km):
        pass

    def alquilar(self, usuario):
        if self.estado:
            if usuario.puede_alquilar(type(self).__name__):
                self.estado = False
                print(f"Vehículo {self.matricula} alquilado a {usuario.nombre}.")
                return True
            else:
                print(f"El usuario {usuario.nombre} no puede alquilar este tipo de vehículo.")
                return False
        else:
            print(f"Vehículo {self.matricula} no está disponible.")
            return False

    def devolver(self, km_final, num_dias):
        self.km += km_final
        self.estado = True
        print(f"Vehículo {self.matricula} devuelto después de {num_dias} días.")

    def mostrar_datos(self):
        estado = "Disponible" if self.estado else "Alquilado"
        return f"Matrícula: {self.matricula}, Kilometraje: {self.km}, Estado: {estado}"
