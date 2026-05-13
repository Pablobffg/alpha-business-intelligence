import matplotlib.pyplot as plt


def cargar_datos():
    ventas = []

    with open("data/datos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea == "":
                continue

            try:
                ventas.append(int(linea))
            except ValueError:
                print("[DATA] Línea ignorada:", linea)

    total = sum(ventas)

    if len(ventas) > 0:
        promedio = total / len(ventas)
    else:
        promedio = 0

    return {
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }


def guardar_venta(nueva_venta):
    with open("data/datos.txt", "a") as f:
        f.write(f"\n{nueva_venta}")


def graficar_ventas(datos, predicciones=None, estrategia=None):

    ventas = datos["ventas"]

    plt.figure()

    plt.plot(ventas, marker="o", label="Ventas reales")

    promedio = datos["promedio"]
    plt.axhline(promedio, linestyle=":", label="Promedio")

    if predicciones:
        inicio = len(ventas) - 1
        x_pred = list(range(inicio, inicio + len(predicciones) + 1))
        y_pred = [ventas[-1]] + predicciones

        plt.plot(x_pred, y_pred, linestyle="--", marker="x", label="Predicción")

    if estrategia:
        plt.text(len(ventas)-1, ventas[-1]+5, f"IA: {estrategia}")

    plt.title("Dashboard Inteligente de Ventas")
    plt.xlabel("Periodo")
    plt.ylabel("Ventas")

    plt.legend()

    plt.show()

def analizar_tendencia(datos):
    ventas = datos["ventas"]

    if len(ventas) < 2:
        print("[IA] No hay suficientes datos para analizar.")
        return

    if ventas[-1] > ventas[-2]:
        print("[IA] Las ventas están subiendo 📈")
    elif ventas[-1] < ventas[-2]:
        print("[IA] Las ventas están bajando 📉")
    else:
        print("[IA] Las ventas se mantienen estables ➖")
       