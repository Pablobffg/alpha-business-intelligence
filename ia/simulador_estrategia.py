import random


def simular_estrategias(datos):

    ventas = datos["ventas"]
    ultima_venta = ventas[-1]

    estrategias = {
        "invertir_marketing": ultima_venta + random.randint(10, 80),
        "bajar_precios": ultima_venta + random.randint(-20, 40),
        "expandir_mercado": ultima_venta + random.randint(20, 100),
        "mantener_estrategia": ultima_venta + random.randint(-10, 20)
    }

    print("\n[SIMULADOR] Probando estrategias...\n")

    for estrategia, resultado in estrategias.items():
        print(f"[SIMULADOR] {estrategia} → ventas estimadas: {resultado}")

    mejor = max(estrategias, key=estrategias.get)

    print("\n[SIMULADOR] Mejor estrategia detectada:", mejor)

    return mejor