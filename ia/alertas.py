def detectar_caida(ventas):
    if len(ventas) < 3:
        return

    if ventas[-1] < ventas[-2] < ventas[-3]:
        print("[ALERTA] Caída consecutiva de ventas")