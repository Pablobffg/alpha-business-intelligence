class MotorDecisiones:
    def decidir(self, datos):
        if datos["promedio"] > 200:
            return "ESCALAR"
        elif datos["promedio"] > 100:
            return "MANTENER"
        else:
            return "OPTIMIZAR"