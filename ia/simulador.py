def simular_futuro(ventas, pasos=5):
    predicciones = []
    datos = ventas.copy()

    for _ in range(pasos):
        ultimas = datos[-3:]
        pred = sum(ultimas) / len(ultimas)
        pred = round(pred)

        predicciones.append(pred)
        datos.append(pred)

    return predicciones
