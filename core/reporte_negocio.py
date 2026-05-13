def generar_reporte(datos, estrategia, prediccion):

    print("\n========== REPORTE ALPHA BUSINESS INTELLIGENCE ==========\n")

    print("Ventas totales:", datos["total"])
    print("Promedio ventas:", round(datos["promedio"],2))

    print("Estrategia IA:", estrategia)
    print("Predicción próxima venta:", prediccion)

    print("\nEstado del sistema: OPERATIVO")

    print("\n========================================================\n")
