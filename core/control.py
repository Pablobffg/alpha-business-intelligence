from core.estado import EstadoSistema

class ControlCentral:
    def __init__(self):
        self.estado = EstadoSistema.INACTIVO

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"[CONTROL] Estado cambiado a: {self.estado}")