class Usuario:
    def __init__(self, cedula, nombre, login, passwd, rol, edad=18, condicion_vision=False, condicion_auditiva=False):
        self.cedula = cedula
        self.nombre = nombre
        self.login = login
        self.passwd = passwd
        self.rol = rol  # profe con el parametro de rol podemos definir si será administrador o usuario
        self.edad = edad
        self.condicion_vision = condicion_vision
        self.condicion_auditiva = condicion_auditiva

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def tiene_restricciones(self):
        "Verifica si el usuario tiene alguna restricción (visión o auditiva)"
        return self.condicion_vision or self.condicion_auditiva

    def puede_alquilar(self, tipo_vehiculo):
        "Determina si el usuario puede alquilar un vehículo según sus restricciones"
    #Si los uduarios son menores de edad no podrán alquilar vheiculos o si tienen problemas de visión o de audición
        return self.es_mayor_de_edad() and not self.tiene_restricciones()


    def __str__(self):
        return (f"Usuario: {self.nombre}, Rol: {self.rol}, Edad: {self.edad}, "
                f"Visión: {self.condicion_vision}, Auditiva: {self.condicion_auditiva}")
 