from .agente_base import AgenteBase

class AgenteControl(AgenteBase):
    def decidir(self, contexto):
        return "mantener_estado"