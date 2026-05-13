class AnalizadorPatrones:

    def analizar(self, ventas):

        tendencia = "estable"

        if ventas[-1] > ventas[0]:
            tendencia = "crecimiento"
        elif ventas[-1] < ventas[0]:
            tendencia = "caida"

        cambios = []
        for i in range(1, len(ventas)):
            cambios.append(ventas[i] - ventas[i-1])

        volatilidad = sum([abs(c) for c in cambios]) / len(cambios)

        if volatilidad > 50:
            estabilidad = "inestable"
        else:
            estabilidad = "estable"

        print("[PATRONES] Tendencia:", tendencia)
        print("[PATRONES] Estabilidad:", estabilidad)
        print("[PATRONES] Volatilidad:", round(volatilidad,2))

        return {
            "tendencia": tendencia,
            "estabilidad": estabilidad,
            "volatilidad": volatilidad
        }