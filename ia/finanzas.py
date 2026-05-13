def calcular_ganancia(datos, precio=20, costo=10):
    ventas = datos["ventas"]
    ganancias = [(v * (precio-costo)) for v in ventas]
    return sum(ganancias)