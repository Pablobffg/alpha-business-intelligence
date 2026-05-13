import os
from motor import MotorSistema

class MotorAutomatizacion:
    def __init__(self, motor: MotorSistema):
        self.motor = motor

    def leer_datos(self):
        self.motor.registrar("Leyendo datos reales...")
        datos = []

        with open("data/datos.txt", "r") as f:
            for linea in f:
                if "ventas=" in linea:
                    valor = int(linea.strip().split("=")[1])
                    datos.append(valor)

        return datos

    def procesar(self, datos):
        self.motor.registrar("Procesando datos...")
        total = sum(datos)
        promedio = total / len(datos)
        return total, promedio

    def generar_reporte(self, total, promedio):
        self.motor.registrar("Generando reporte...")

        # crear carpeta outputs si no existe
        if not os.path.exists("outputs"):
            os.mkdir("outputs")

        with open("outputs/reporte.txt", "w") as f:
            f.write(f"Total ventas: {total}\n")
            f.write(f"Promedio ventas: {promedio}\n")

    def ciclo(self):
        datos = self.leer_datos()
        total, promedio = self.procesar(datos)
        self.generar_reporte(total, promedio)
        print("Reporte generado en outputs/reporte.txt")


if __name__ == "__main__":
    sistema = MotorSistema("AlphaCore")
    sistema.iniciar()

    automatizador = MotorAutomatizacion(sistema)
    automatizador.ciclo()

    sistema.detener()