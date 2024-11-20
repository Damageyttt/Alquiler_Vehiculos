import csv
from models.moto import Moto
from models.coche import Coche
from models.furgoneta import Furgoneta

class GestionVehiculosService:
    def __init__(self):
        #Estos son los vehiculos que seleccionamos como predeterminados
        self.vehiculos = [
            Moto("TVU99D", 1000, casco=True),
            Moto("CDA98U", 3500, casco=False),
            Moto("DSA22E", 13000, casco=True),
            Coche("ABC123", 5000, extras=True),
            Coche("AAO111", 35000, extras=False),
            Furgoneta("XYZ456", 20000, capacidad=5)
        ]

    def listar_vehiculos(self):
        "Lista todos los vehículos disponibles y alquilados"
        if not self.vehiculos:
            return "No hay vehículos registrados."
        return [vehiculo.mostrar_datos() for vehiculo in self.vehiculos]

    def buscar_vehiculo(self, matricula):
        "Busca un vehículo por su matrícula"
        for veh in self.vehiculos:
            if veh.matricula == matricula:
                return veh
        return None

    def crear_vehiculo(self, tipo, matricula, km, extra_info):
        "Crea un nuevo vehículo y lo añade a la lista"
        if any(veh.matricula == matricula for veh in self.vehiculos):
            return f"Error: Ya existe un vehículo con la matrícula {matricula}."
        if tipo == "Moto":
            casco =  str(extra_info).lower() in ["true"]
            nuevo_vehiculo = Moto(matricula, km, casco=casco)
        elif tipo == "Coche":
            extras = str(extra_info).lower() in {"true"}
            nuevo_vehiculo = Coche(matricula, km, extras=extra_info)
        elif tipo == "Furgoneta":
            nuevo_vehiculo = Furgoneta(matricula, km, capacidad=extra_info)
        else:
            return "Error: Tipo de vehículo no válido."
        self.vehiculos.append(nuevo_vehiculo)
        return f"Vehículo {tipo} con matrícula {matricula} creado."

    def editar_vehiculo(self, matricula, nuevo_km=None, nuevo_estado=None, nuevo_valor_alquiler=None):
        "Edita las características de un vehículo que ya está"
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo:
            if nuevo_km is not None:
                vehiculo.km = nuevo_km
            if nuevo_estado is not None:
                vehiculo.estado = nuevo_estado
            if nuevo_valor_alquiler is not None:
                vehiculo.valor_alquiler = nuevo_valor_alquiler
            return f"Vehículo {matricula} actualizado exitosamente."
        return "Error: Vehículo no encontrado."

    def eliminar_vehiculo(self, matricula):
        "Elimina un vehículo de la lista"
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo:
            self.vehiculos.remove(vehiculo)
            return f"Vehículo {matricula} eliminado."
        return "Error: Vehículo no encontrado."

    def devolver_vehiculo(self, matricula, km_recorridos, dias_alquiler):
        "Permite devolver un vehículo alquilado"
        vehiculo = self.buscar_vehiculo(matricula)
        if  not vehiculo:
            return f"Error: No se encontró un vehiculo con la matricula {matricula}."
        if vehiculo.estado :
            return f"Error: El vehiculo {matricula} ya está disponible. No se puede devolver"
        vehiculo.devolver(km_recorridos, dias_alquiler)
        return "Devuelto exitosamente."

    def alquilar_vehiculo(self, usuario, matricula):
        "Permite a un usuario alquilar un vehículo si cumple con las restricciones"
        vehiculo = self.buscar_vehiculo(matricula)
        if not vehiculo:
            return f"Error: No se encontró un vehículo con la matrícula {matricula}."

        if not vehiculo.estado:  
            return f"Error: El vehículo {matricula} no está disponible."

        if not usuario.puede_alquilar(type(vehiculo).__name__):
            return f"Error: El usuario {usuario.nombre} no puede alquilar este tipo de vehículo debido a restricciones."

        vehiculo.alquilar(usuario)
        return f"Vehículo {matricula} alquilado exitosamente por {usuario.nombre}."


    def cargar_vehiculos_csv(self, archivo_csv):
        "Carga vehículos desde un archivo CSV"
        try:
            with open(archivo_csv, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tipo = row["tipo"]
                    matricula = row["matricula"]
                    km = int(row["km"])
                    extra_info = row["extra_info"]

                    if tipo == "Moto":
                        nuevo_vehiculo = Moto(matricula, km, casco=extra_info.lower() == "true")
                    elif tipo == "Coche":
                        nuevo_vehiculo = Coche(matricula, km, extras=extra_info.lower() == "true")
                    elif tipo == "Furgoneta":
                        nuevo_vehiculo = Furgoneta(matricula, km, capacidad=int(extra_info))
                    else:
                        return f"Error: Tipo de vehículo no válido en la fila con matrícula {matricula}"

                    self.vehiculos.append(nuevo_vehiculo)
            return "Vehículos cargados exitosamente desde el archivo CSV."
        except Exception as e:
            return f"Error al cargar el archivo CSV: {str(e)}"