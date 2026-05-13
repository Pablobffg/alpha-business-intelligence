from .agente_base import AgenteBase

class AgenteOptimizacion(AgenteBase):
    def decidir(self, contexto):
        return "optimizar_procesos"