def detectar_caida(ventas):
    if len(ventas) < 4:
        print("[ALERTA] No hay suficientes datos para detectar caídas")
        return

    ultimas = ventas[-4:]

    if ultimas[3] < ultimas[2] < ultimas[1]:
        print("[ALERTA] Caída fuerte detectada en ventas 📉")
        print("[IA] Recomendación: revisar estrategia o reducir gastos")
    else:
        print("[SISTEMA] No se detecta caída importante")