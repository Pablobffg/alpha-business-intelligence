def guardar_estrategia(estrategia, ventas_actuales):

    with open("data/memoria_estrategias.txt", "a") as f:
        f.write(f"{estrategia},{ventas_actuales}\n")

    print("[MEMORIA IA] Estrategia guardada:", estrategia)
