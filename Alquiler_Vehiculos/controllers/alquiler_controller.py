from services.gestion_vehiculos import GestionVehiculosService
from services.gestion_usuarios import GestionUsuariosService
from services.pdf_generator import generar_resumen_pdf


class AlquilerVehiculosController:
    def __init__(self):
        self.gestion_vehiculos = GestionVehiculosService()
        self.gestion_usuarios = GestionUsuariosService()

        # Profe con este metodo podremos registrarnos en la interfaz como administrador
        self.registrar_usuario(
            cedula="00000000",
            nombre="Admin",
            login="admin",
            passwd="admin123",
            rol="admin",
            edad=30,
            condicion_vision=False,
            condicion_auditiva=False
        )

    def registrar_usuario(self, cedula, nombre, login, passwd, rol, edad=18, condicion_vision=False, condicion_auditiva=False):
        "Llama al servicio para registrar un nuevo usuario con validaciones"
        return self.gestion_usuarios.registrar_usuario(cedula, nombre, login, passwd, rol, edad, condicion_vision, condicion_auditiva)

    def alquilar_vehiculo(self, usuario_login, passwd, matricula):
        "Llama al servicio para realizar el alquiler de un vehículo"
        usuario = self.validar_usuario(usuario_login, passwd)
        if not usuario:
            return "Error: Usuario no encontrado"
        return self.gestion_vehiculos.alquilar_vehiculo(usuario, matricula)


    def validar_usuario(self, login, passwd):
        "Valida los datos del usuario y devuelve el objeto Usuario si son correctas"
        usuario = self.gestion_usuarios.validar_usuario(login, passwd)
        return usuario  

    def listar_usuarios(self):
        "Lista todos los usuarios registrados"
        return self.gestion_usuarios.listar_usuarios()

    def listar_vehiculos(self):
        "Lista todos los vehículos registrados"
        return self.gestion_vehiculos.listar_vehiculos()

    def crear_vehiculo(self, tipo, matricula, km, extra_info):
        "Crea un nuevo vehículo"
        return self.gestion_vehiculos.crear_vehiculo(tipo, matricula, km, extra_info)

    def eliminar_vehiculo(self, matricula):
        "Elimina un vehículo"
        return self.gestion_vehiculos.eliminar_vehiculo(matricula)

    def editar_vehiculo(self, matricula, nuevo_km=None, nuevo_estado=None, nuevo_valor_alquiler=None):
        "Edita un vehículo existente"
        return self.gestion_vehiculos.editar_vehiculo(matricula, nuevo_km, nuevo_estado, nuevo_valor_alquiler)

    def devolver_vehiculo(self, matricula, km_recorridos, dias_alquiler):
        "Permite devolver un vehículo alquilado"
        return self.gestion_vehiculos.devolver_vehiculo(matricula, km_recorridos, dias_alquiler)

    def cargar_vehiculos_csv(self, archivo_csv):
        "Carga vehículos desde un archivo CSV"
        return self.gestion_vehiculos.cargar_vehiculos_csv(archivo_csv)

    def generar_resumen_pdf(self, archivo_pdf):
        "Genera un resumen de vehículos en formato PDF"
        vehiculos = self.gestion_vehiculos.vehiculos
        generar_resumen_pdf(vehiculos, archivo_pdf)
        return "Resumen PDF generado"