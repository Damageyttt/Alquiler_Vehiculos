from tkinter import Tk, Label, Button, Entry, Text, Toplevel, END

class AlquilerVehiculosGUI:
    def __init__(self, controller):
        self.controller = controller
        self.usuario_actual = None
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.eval('tk::PlaceWindow . center')
        self.root.title("Sistema de Alquiler de Vehículos")
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        "Interfaz inicial para el inicio de sesión"
        self.limpiar_interfaz()
        Label(self.root, text="Login del Sistema", font=("Arial", 16)).pack(pady=10)
        Label(self.root, text="Login:").pack()
        self.login_entry = Entry(self.root)
        self.login_entry.pack()
        Label(self.root, text="Contraseña:").pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()
        Button(self.root, text="Ingresar", command=self.validar_login).pack(pady=10)
        self.salida = Label(self.root, text="")
        self.salida.pack()

    def validar_login(self):
        "Valida el inicio de sesión"
        login = self.login_entry.get()
        passwd = self.password_entry.get()
        usuario = self.controller.validar_usuario(login, passwd)
        if usuario:
            self.usuario_actual = usuario
            self.crear_interfaz_principal()
        else:
            self.salida.config(text="datos incorrectos. Intente nuevamente.", fg="red")

    def crear_interfaz_principal(self):
        "Interfaz principal después del inicio de sesión"
        self.limpiar_interfaz()
        Label(self.root, text=f"Bienvenido, {self.usuario_actual.nombre} ({self.usuario_actual.rol})", font=("Arial", 16)).pack(pady=10)
        if self.usuario_actual.rol == "admin":
            self.crear_menu_administrador()
        elif self.usuario_actual.rol == "usuario":
            self.crear_menu_usuario()
        Button(self.root, text="Cerrar Sesión", command=self.crear_interfaz_login).pack(pady=10)

    def crear_menu_administrador(self):
        "Opciones específicas para administradores"
        Button(self.root, text="Listar Vehículos", command=self.listar_vehiculos).pack(pady=5)
        Button(self.root, text="Crear Vehículo", command=self.mostrar_crear_vehiculo).pack(pady=5)
        Button(self.root, text="Editar Vehículo", command=self.mostrar_editar_vehiculo).pack(pady=5)
        Button(self.root, text="Eliminar Vehículo", command=self.mostrar_eliminar_vehiculo).pack(pady=5)
        Button(self.root, text="Validar Devolución", command=self.mostrar_validar_devolucion).pack(pady=5)
        Button(self.root, text="Listar Usuarios", command=self.listar_usuarios).pack(pady=5)
        Button(self.root, text="Crear Usuario", command=self.mostrar_crear_usuario).pack(pady=5)  # NUEVO
        Button(self.root, text="Cargar Vehículos (CSV)", command=self.cargar_vehiculos_csv).pack(pady=5)
        Button(self.root, text="Generar Resumen PDF", command=self.generar_resumen_pdf).pack(pady=5)



    def mostrar_crear_usuario(self):
        "Ventana para registrar un nuevo usuario"
        ventana = Toplevel(self.root)
        ventana.title("Crear Usuario")

        Label(ventana, text="Cédula:").pack()
        cedula = Entry(ventana)
        cedula.pack()

        Label(ventana, text="Nombre:").pack()
        nombre = Entry(ventana)
        nombre.pack()

        Label(ventana, text="Login:").pack()
        login = Entry(ventana)
        login.pack()

        Label(ventana, text="Contraseña:").pack()
        passwd = Entry(ventana, show="*")
        passwd.pack()

        Label(ventana, text="Rol (admin/usuario):").pack()
        rol = Entry(ventana)
        rol.pack()

        Label(ventana, text="Edad:").pack()
        edad = Entry(ventana)
        edad.pack()

        Label(ventana, text="¿Tiene problemas de visión? (s/n):").pack()
        condicion_vision = Entry(ventana)
        condicion_vision.pack()

        Label(ventana, text="¿Tiene problemas auditivos? (s/n):").pack()
        condicion_auditiva = Entry(ventana)
        condicion_auditiva.pack()

        def realizar_accion():
            try:
                resultado = self.controller.registrar_usuario(
                    cedula.get(),
                    nombre.get(),
                    login.get(),
                    passwd.get(),
                    rol.get(),
                    int(edad.get()),
                    condicion_vision.get().lower() == "s",
                    condicion_auditiva.get().lower() == "s"
                )
                self.mostrar_resultado(resultado)
                ventana.destroy()
            except Exception as e:
                self.mostrar_resultado(f"Error: {str(e)}")
                ventana.destroy()

        Button(ventana, text="Confirmar", command=realizar_accion).pack(pady=10)


    def crear_menu_usuario(self):
        "Opciones específicas para usuarios"
        Button(self.root, text="Listar Vehículos Disponibles", command=self.listar_vehiculos_disponibles).pack(pady=5)
        Button(self.root, text="Alquilar Vehículo", command=self.mostrar_alquilar_vehiculo).pack(pady=5)

    def listar_vehiculos(self):
        "Muestra todos los vehículos"
        self.mostrar_resultado("\n".join(self.controller.listar_vehiculos()))

    def listar_vehiculos_disponibles(self):
        "Muestra los vehículos disponibles"
        vehiculos = [v for v in self.controller.listar_vehiculos() if "Disponible" in v]
        self.mostrar_resultado("\n".join(vehiculos))

    def listar_usuarios(self):
        "Muestra todos los usuarios registrados"
        self.mostrar_resultado("\n".join(self.controller.listar_usuarios()))

    def mostrar_crear_vehiculo(self):
        """Ventana para crear un nuevo vehículo"
        self.crear_ventana_vehiculo("Crear Vehículo", self.controller.crear_vehiculo)

    def mostrar_editar_vehiculo(self):
        "Ventana para editar un vehículo existente."""
        ventana = Toplevel(self.root)
        ventana.title("Editar Vehículo")

        Label(ventana, text="Matrícula:").pack()
        matricula = Entry(ventana)
        matricula.pack()

        Label(ventana, text="Nuevo Kilometraje:").pack()
        km = Entry(ventana)
        km.pack()

        Label(ventana, text="¿Está disponible? (s/n):").pack()
        estado = Entry(ventana)
        estado.pack()

        Label(ventana, text="Nuevo Valor de Alquiler:").pack()
        valor_alquiler = Entry(ventana)
        valor_alquiler.pack()

        def realizar_accion():
            estado_bool = True if estado.get().lower() == "s" else False if estado.get().lower() == "n" else None
            resultado = self.controller.editar_vehiculo(
                matricula.get(),
                nuevo_km=int(km.get()) if km.get() else None,
                nuevo_estado=estado_bool,
                nuevo_valor_alquiler=float(valor_alquiler.get()) if valor_alquiler.get() else None
            )
            self.mostrar_resultado(resultado)
            ventana.destroy()

        Button(ventana, text="Confirmar", command=realizar_accion).pack(pady=10)

    def mostrar_eliminar_vehiculo(self):
        "Ventana para eliminar un vehículo"
        self.crear_ventana_simple("Eliminar Vehículo", "Matrícula:", self.controller.eliminar_vehiculo)

    def mostrar_alquilar_vehiculo(self):
        "Ventana para alquilar un vehículo"
        ventana = Toplevel(self.root)
        ventana.title("Alquilar Vehículo")

        Label(ventana, text="Login del Usuario:").pack()
        login = Entry(ventana)
        login.pack()

        Label(ventana, text="Contraseña:").pack()
        passwd = Entry(ventana, show="*")
        passwd.pack()

        Label(ventana, text="Matrícula del Vehículo:").pack()
        matricula = Entry(ventana)
        matricula.pack()

        def realizar_accion():
            resultado = self.controller.alquilar_vehiculo(login.get(), passwd.get(), matricula.get())
            self.mostrar_resultado(resultado)
            ventana.destroy()

        Button(ventana, text="Confirmar", command=realizar_accion).pack(pady=10)

    def mostrar_validar_devolucion(self):
        "Ventana para validar la devolución de un vehículo"
        ventana = Toplevel(self.root)
        ventana.title("Validar Devolución")

        Label(ventana, text="Matrícula:").pack()
        matricula = Entry(ventana)
        matricula.pack()

        Label(ventana, text="Kilómetros Recorridos:").pack()
        km = Entry(ventana)
        km.pack()

        Label(ventana, text="Días de Alquiler:").pack()
        dias = Entry(ventana)
        dias.pack()

        def realizar_accion():
            try:    
                resultado = self.controller.devolver_vehiculo(matricula.get(), int(km.get()), int(dias.get()))
                self.mostrar_resultado(resultado)
            except Exception as e:
                self.mostrar_resultado(f"error:{str(e)}")
            ventana.destroy()

        Button(ventana, text="Confirmar", command=realizar_accion).pack(pady=10)

    def mostrar_resultado(self, texto):
        "Muestra el resultado de una acción"
        self.limpiar_interfaz()
        Label(self.root, text="Resultado:", font=("Arial", 14)).pack(pady=10)
        resultado = Text(self.root, wrap="word", height=15, width=50)
        resultado.pack(pady=10)
        resultado.insert(END, texto)
        Button(self.root, text="Volver al Menú", command=self.crear_interfaz_principal).pack(pady=10)

    def cargar_vehiculos_csv(self):
        "Ventana para cargar un archivo CSV con vehículos"
        from tkinter.filedialog import askopenfilename

        archivo_csv = askopenfilename(
            title="Seleccionar Archivo CSV",
            filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
        )

        if archivo_csv:
            try:
                resultado = self.controller.cargar_vehiculos_csv(archivo_csv)
                self.mostrar_resultado(resultado)
            except Exception as e:
                self.mostrar_resultado(f"Error: {str(e)}")

    def generar_resumen_pdf(self):
        "Genera un archivo PDF con el resumen de vehículos agrupados"
        try:
            archivo_pdf = "resumen_vehiculos.pdf"  # Nombre del archivo generado
            resultado = self.controller.generar_resumen_pdf(archivo_pdf)
            self.mostrar_resultado(f"Resumen PDF generado: {archivo_pdf}")
        except Exception as e:
            self.mostrar_resultado(f"Error: {str(e)}")


    def crear_ventana_vehiculo(self, titulo, accion):
        "Ventana genérica para la creación o edición de vehículos"
        ventana = Toplevel(self.root)
        ventana.title(titulo)

        Label(ventana, text="Matrícula:").pack()
        matricula = Entry(ventana)
        matricula.pack()

        Label(ventana, text="Kilómetros:").pack()
        km = Entry(ventana)
        km.pack()

        Label(ventana, text="Información Adicional (Ejemplo: Casco/Extras/Capacidad):").pack()
        info = Entry(ventana)
        info.pack()

        Label(ventana, text="Tipo de Vehículo (Moto, Coche, Furgoneta):").pack()
        tipo = Entry(ventana)
        tipo.pack()

        def realizar_accion():
            try:
                resultado = accion(tipo.get(), matricula.get(), int(km.get()), info.get())
                self.mostrar_resultado(resultado)
                ventana.destroy()
            except Exception as e:
                self.mostrar_resultado(f"Error: {str(e)}")
                ventana.destroy()

        Button(ventana, text="Confirmar", command=realizar_accion).pack(pady=10)

    def crear_ventana_simple(self, titulo, etiqueta, accion):
        "Ventana simple para ingresar datos y ejecutar una acción"
        ventana = Toplevel(self.root)
        ventana.title(titulo)
        Label(ventana, text=etiqueta).pack()
        entrada = Entry(ventana)
        entrada.pack()

        def realizar_accion():
            resultado = accion(entrada.get())
            self.mostrar_resultado(resultado)
            ventana.destroy()

        Button(ventana, text="Confirmar", command=realizar_accion).pack(pady=10)

    def limpiar_interfaz(self):
        "Elimina todos los widgets de la ventana principal"
        for widget in self.root.winfo_children():
            widget.destroy()

    def iniciar(self):
        "Inicia la interfaz gráfica"
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Error inesperado: {e}")
            
            from tkinter import Tk, Label, Frame

class VehiculosGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Lista de Vehículos")
        self.root.geometry("400x300")

        self.vehiculos = [
            {"tipo": "Auto", "matricula": "ABC123", "color": "red"},
            {"tipo": "Auto", "matricula": "DEF456", "color": "red"},
            {"tipo": "Auto", "matricula": "GHI789", "color": "red"},
            {"tipo": "Moto", "matricula": "MOT001", "color": "red"},
        ]

        self.mostrar_vehiculos()

    def mostrar_vehiculos(self):
        "Crea una interfaz con la lista de vehículos en colores personalizados"
        frame =  any Frame(self.root)
        frame.pack(pady=10)

        for vehiculo in self.vehiculos:
            texto = f"{vehiculo['tipo']} - Matrícula: {vehiculo['matricula']}"
            Label(frame, text=texto, fg=vehiculo["color"]).pack(pady=5)

    def iniciar(self):
        "Inicia la aplicación"
        self.root.mainloop()


if __name__ == "__main__":
    gui = VehiculosGUI()
    gui.iniciar()
