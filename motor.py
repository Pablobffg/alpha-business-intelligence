class MotorSistema:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "inicializado"
        self.logs = []

    def registrar(self, mensaje):
        self.logs.append(mensaje)
        print(f"[LOG] {mensaje}")

    def iniciar(self):
        self.estado = "activo"
        self.registrar(f"Sistema {self.nombre} iniciado")

    def detener(self):
        self.estado = "detenido"
        self.registrar(f"Sistema {self.nombre} detenido")

    def estado_actual(self):
        return self.estado


if __name__ == "__main__":
    sistema = MotorSistema("AlphaCore")
    sistema.iniciar()
    print("Estado actual:", sistema.estado_actual())
    sistema.detener()