from .agente_base import AgenteBase

class AgenteAnalisis(AgenteBase):
    def decidir(self, contexto):
        if contexto["promedio"] > 150:
            return "mantener_estado"
        return "alerta_riesgo"