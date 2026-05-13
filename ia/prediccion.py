def predecir_venta(ventas):
    if len(ventas) < 3:
        return ventas[-1]

    ultimas = ventas[-3:]
    prediccion = sum(ultimas) / len(ultimas)

    return round(prediccion)