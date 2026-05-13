def decidir_estrategia(mejor_simulada, mejor_historica, patrones):
    if mejor_historica:
        desicion = mejor_historica
    else:
        desicion = mejor_simulada

    if patrones["tendencia"] == "bajando":
        desicion = "invertir_marketing"

    return desicion