from controllers.alquiler_controller import AlquilerVehiculosController
from gui import AlquilerVehiculosGUI

def main():
    print("Iniciando la interfaz gráfica...")
    controller = AlquilerVehiculosController()
    gui = AlquilerVehiculosGUI(controller)
    gui.iniciar()  #Aquí inciamos la interfaz grafica profe

if __name__ == "__main__":
    main()
