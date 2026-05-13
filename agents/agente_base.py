class AgenteBase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "activo"

    def percibir(self, datos):
        return datos

    def decidir(self, contexto):
        pass

    def actuar(self, decision):
        print(f"[AGENTE {self.nombre}] Ejecutando:", decision)