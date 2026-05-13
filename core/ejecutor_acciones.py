def ejecutar_accion(estrategia):

    print("\n[ALPHA CONTROL] Ejecutando estrategia...\n")

    if estrategia == "invertir_marketing":
        print("[ACCION] Activando campaña de marketing")

    elif estrategia == "bajar_precios":
        print("[ACCION] Ajustando precios del producto")

    elif estrategia == "expandir_mercado":
        print("[ACCION] Buscando nuevos mercados")

    elif estrategia == "mantener_estrategia":
        print("[ACCION] Manteniendo estrategia actual")

    else:
        print("[ACCION] Estrategia desconocida")

    print("\n[ALPHA CONTROL] Acción ejecutada correctamente")