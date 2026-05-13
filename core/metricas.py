# core/metricas.py

class SistemaMetricas:
    def __init__(self):
        self.total_decisiones = 0
        self.decisiones_exitosas = 0
        self.expansiones = 0
        self.optimizaciones = 0

    def registrar_decision(self, decision, resultado="positivo"):
        self.total_decisiones += 1
        
        if resultado == "positivo":
            self.decisiones_exitosas += 1

        if decision == "escalar_sistema":
            self.expansiones += 1

        if decision == "optimizar_procesos":
            self.optimizaciones += 1

    def tasa_exito(self):
        if self.total_decisiones == 0:
            return 0
        return self.decisiones_exitosas / self.total_decisiones

    def resumen(self):
        return {
            "total_decisiones": self.total_decisiones,
            "tasa_exito": self.tasa_exito(),
            "expansiones": self.expansiones,
            "optimizaciones": self.optimizaciones
        }