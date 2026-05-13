class MotorReglas:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def evaluar(self, contexto):
        resultados = []
        for regla in self.reglas:
            if regla(contexto):
                resultados.append(regla.__name__)
        return resultados