from models.usuario import Usuario

class GestionUsuariosService:
    def __init__(self):
        "el constructor da inicio a la lista de usuarios"
        self.usuarios = []  # Profe esta será la lista para almacenar los usuarios

    def registrar_usuario(self, cedula, nombre, login, passwd, rol, edad=18, condicion_vision=False, condicion_auditiva=False):
        "Registra un nuevo usuario si no tiene restricciones o no es menor de edad"
        if edad < 18:
            return "Error: Los usuarios menores de edad no pueden registrarse."
        if condicion_vision or condicion_auditiva:
            return "Error: Los usuarios con restricciones de visión o auditivas no pueden registrarse."

        if any(usuario.cedula == cedula for usuario in self.usuarios):
            return f"Error: Ya existe un usuario con la cédula {cedula}."

        nuevo_usuario = Usuario(cedula, nombre, login, passwd, rol, edad, condicion_vision, condicion_auditiva)
        self.usuarios.append(nuevo_usuario)
        return f"Usuario {nombre} registrado exitosamente."

    def listar_usuarios(self):
        "Devuelve una lista de los usuarios registrados"
        if not self.usuarios:
            return "No hay usuarios registrados."
        return [f"Cédula: {usuario.cedula}, Nombre: {usuario.nombre}, Rol: {usuario.rol}" for usuario in self.usuarios]

    def validar_usuario(self, login, passwd):
        "Valida el inicio de sesion de un usuario y devuelve el objeto Usuario si sus datos son correctos"
        for usuario in self.usuarios:
            if usuario.login == login and usuario.passwd == passwd:
                return usuario 
        return None  
