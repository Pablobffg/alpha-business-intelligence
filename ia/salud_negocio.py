def evaluar_salud(ventas):

    if len(ventas) < 5:
        print("[SALUD NEGOCIO] Datos insuficientes")
        return

    promedio = sum(ventas) / len(ventas)
    ultimas = ventas[-5:]

    ult_prom = sum(ultimas) / len(ultimas)

    if ult_prom > promedio * 1.1:
        estado = "crecimiento fuerte 📈"

    elif ult_prom < promedio * 0.9:
        estado = "riesgo de caída ⚠️"

    else:
        estado = "estable ➖"

    print(f"[SALUD NEGOCIO] Estado actual: {estado}")