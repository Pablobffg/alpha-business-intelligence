class DecisionInteligente:

    def decidir(self, mejor_historial, patrones, datos):

        tendencia = patrones["tendencia"]
        estabilidad = patrones["estabilidad"]

        # 🔥 lógica híbrida
        if tendencia == "caida":
            decision = "invertir_en_marketing"

        elif tendencia == "crecimiento" and estabilidad == "estable":
            decision = mejor_historial

        elif estabilidad == "inestable":
            decision = "mantener_estrategia"

        else:
            decision = mejor_historial

        print("[IA DIOS] Decisión final:", decision)

        return decision