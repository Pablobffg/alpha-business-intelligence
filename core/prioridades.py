class MotorPrioridades:
    def asignar(self, decision):
        prioridades = {
            "ESCALAR": 1,
            "MANTENER": 2,
            "OPTIMIZAR": 3
        }
        return prioridades.get(decision, 99)