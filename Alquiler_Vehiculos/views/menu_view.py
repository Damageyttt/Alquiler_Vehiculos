class MenuView:
    def __init__(self, controller):
        self.controller = controller

    def mostrar_menu(self):
        while True:
            print("\n=== Menú Principal ===")
            print("1. Registrar Usuario")
            print("2. Listar Usuarios")
            print("3. Listar Vehículos")
            print("4. Crear Vehículo")
            print("5. Editar Vehículo")
            print("6. Validar Devolución")
            print("7. Alquilar Vehículo")
            print("8. Generar Reporte de Usuarios")
            print("9. Generar Reporte de Vehículos")
            print("10. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.listar_usuarios()
            elif opcion == "3":
                self.listar_vehiculos()
            elif opcion == "4":
                self.crear_vehiculo()
            elif opcion == "5":
                self.editar_vehiculo()
            elif opcion == "6":
                self.validar_devolucion()
            elif opcion == "7":
                self.alquilar_vehiculo()
            elif opcion == "8":
                self.generar_reporte_usuarios()
            elif opcion == "9":
                self.generar_reporte_vehiculos()
            elif opcion == "10":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def registrar_usuario(self):
        print("\n--- Registrar Usuario ---")
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        login = input("Login: ")
        passwd = input("Contraseña: ")
        rol = input("Rol (admin/usuario): ").lower()
        edad = int(input("Edad: "))
        condicion_vision = input("¿Tiene problemas de visión? (s/n): ").lower() == "s"
        condicion_auditiva = input("¿Tiene problemas auditivos? (s/n): ").lower() == "s"
        resultado = self.controller.registrar_usuario(
            cedula, nombre, login, passwd, rol, edad, condicion_vision, condicion_auditiva
        )
        print(resultado)

    def listar_usuarios(self):
        print("\n--- Lista de Usuarios ---")
        usuarios = self.controller.listar_usuarios()
        print("\n".join(usuarios) if isinstance(usuarios, list) else usuarios)

    def listar_vehiculos(self):
        print("\n--- Lista de Vehículos ---")
        vehiculos = self.controller.listar_vehiculos()
        print("\n".join(vehiculos) if isinstance(vehiculos, list) else vehiculos)

    def crear_vehiculo(self):
        print("\n--- Crear Vehículo ---")
        tipo = input("Tipo (Moto/Coche/Furgoneta): ")
        matricula = input("Matrícula: ")
        km = int(input("Kilómetros: "))
        extra_info = input("Casco (s/n) para Moto, Extras (s/n) para Coche, Capacidad (número) para Furgoneta: ")
        extra_info = True if extra_info.lower() == "s" else (int(extra_info) if tipo == "Furgoneta" else False)
        resultado = self.controller.crear_vehiculo(tipo, matricula, km, extra_info)
        print(resultado)

    def editar_vehiculo(self):
        print("\n--- Editar Vehículo ---")
        matricula = input("Matrícula del vehículo a editar: ")
        nuevo_km = input("Nuevo kilometraje (dejar vacío para no cambiar): ")
        nuevo_estado = input("¿Está disponible? (s/n, dejar vacío para no cambiar): ")
        nuevo_valor_alquiler = input("Nuevo valor de alquiler (dejar vacío para no cambiar): ")

        nuevo_km = int(nuevo_km) if nuevo_km else None
        nuevo_estado = True if nuevo_estado.lower() == "s" else (False if nuevo_estado.lower() == "n" else None)
        nuevo_valor_alquiler = float(nuevo_valor_alquiler) if nuevo_valor_alquiler else None

        resultado = self.controller.editar_vehiculo(
            matricula, nuevo_km, nuevo_estado, nuevo_valor_alquiler
        )
        print(resultado)

    def validar_devolucion(self):
        print("\n--- Validar Devolución ---")
        matricula = input("Matrícula del vehículo: ")
        km_recorridos = int(input("Kilómetros recorridos: "))
        dias_alquiler = int(input("Días de alquiler: "))
        resultado = self.controller.devolver_vehiculo(matricula, km_recorridos, dias_alquiler)
        print(resultado)

    def alquilar_vehiculo(self):
        print("\n--- Alquilar Vehículo ---")
        login = input("Login del usuario: ")
        passwd = input("Contraseña del usuario: ")
        matricula = input("Matrícula del vehículo: ")
        resultado = self.controller.alquilar_vehiculo(login, passwd, matricula)
        print(resultado)

    def generar_reporte_usuarios(self):
        print("\n--- Reporte de Usuarios ---")
        reporte = self.controller.generar_reporte_usuarios()
        print(reporte)

    def generar_reporte_vehiculos(self):
        print("\n--- Reporte de Vehículos ---")
        reporte = self.controller.generar_reporte_vehiculos()
        print(reporte)
