from models.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, cedula, nombre, login, passwd, edad=18, condicion_vision=False, condicion_auditiva=False):
        super().__init__(cedula, nombre, login, passwd, "usuario", edad, condicion_vision, condicion_auditiva)

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"
