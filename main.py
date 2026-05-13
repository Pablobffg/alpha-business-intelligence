import time
from core.metricas import SistemaMetricas
from core.reporte_negocio import generar_reporte
from core.ejecutor_acciones import ejecutar_accion
from core.decisor_negocios import decidir_estrategia
from data.lector_datos import cargar_datos, guardar_venta, graficar_ventas, analizar_tendencia
from ia.prediccion import predecir_venta
from ia.simulador import simular_futuro
from ia.detector_caida import detectar_caida
from ia.salud_negocio import evaluar_salud
from ia.simulador_estrategia import simular_estrategias
from ia.memoria_estrategica import guardar_estrategia
from ia.analizador_patrones import AnalizadorPatrones
from ia.evaluador_estrategias import EvaluadorEstrategias
from ia.decision_inteligente import DecisionInteligente
from ia.finanzas import calcular_ganancia


def ejecutar_ciclo_completo():
    datos = cargar_datos()
    metricas = SistemaMetricas()
    evaluador = EvaluadorEstrategias()

    # Simulación y estrategia
    mejor = simular_estrategias(datos)
    guardar_estrategia(mejor, datos["ventas"][-1])
    ejecutar_accion(mejor)

    # Análisis
    ventas = datos["ventas"]
    patrones = AnalizadorPatrones().analizar(ventas)
    futuro = simular_futuro(ventas)
    pred = predecir_venta(ventas)

    # Evaluador con aprendizaje
    if len(ventas) >= 2:
        resultado = 1 if ventas[-1] > ventas[-2] else 0
        evaluador.registrar(mejor, resultado)
        mejor_aprendido = evaluador.evaluar()
        if mejor_aprendido:
            mejor = mejor_aprendido

    # Decisión final
    decision_final = DecisionInteligente().decidir(mejor, patrones, datos)

    # Alertas y salud
    detectar_caida(ventas)
    evaluar_salud(ventas)

    # Reporte
    generar_reporte(datos, mejor, futuro[0])
    print(f"[PREDICCION] Próxima venta: {pred}")
    print(f"[DECISION FINAL] {decision_final}")
    print(f"[GANANCIAS] {calcular_ganancia(datos)}")

    guardar_venta(pred)
    graficar_ventas(datos, futuro, mejor)


if __name__ == "__main__":
    while True:
        ejecutar_ciclo_completo()
        time.sleep(5)