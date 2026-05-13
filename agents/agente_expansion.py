from .agente_base import AgenteBase

class AgenteExpansion(AgenteBase):
    def decidir(self, contexto):
        if contexto["total"] > 800:
            return "escalar_sistema"
        return "esperar"