from flask import Flask, jsonify, request
from data.lector_datos import cargar_datos, guardar_venta
from ia.prediccion import predecir_venta
from ia.simulador import simular_futuro
from ia.simulador_estrategia import simular_estrategias
from ia.finanzas import calcular_ganancia
from core.reporte_negocio import generar_reporte
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/reporte", methods=["GET"])
def reporte():
    datos = cargar_datos()
    mejor = simular_estrategias(datos)
    futuro = simular_futuro(datos["ventas"])
    return jsonify({
        "estrategia": mejor,
        "ventas_totales": datos["total"],
        "promedio": round(datos["promedio"], 2),
        "estado": "operativo"
    })


@app.route("/prediccion", methods=["GET"])
def prediccion():
    datos = cargar_datos()
    ventas = datos["ventas"]
    pred = predecir_venta(ventas)
    futuro = simular_futuro(ventas)
    return jsonify({
        "proxima_venta": pred,
        "simulacion_5_periodos": futuro
    })


@app.route("/venta", methods=["POST"])
def agregar_venta():
    body = request.get_json()
    if not body or "cantidad" not in body:
        return jsonify({"error": "Falta el campo cantidad"}), 400
    guardar_venta(body["cantidad"])
    return jsonify({"mensaje": "Venta registrada", "cantidad": body["cantidad"]})


@app.route("/metricas", methods=["GET"])
def metricas():
    datos = cargar_datos()
    ganancias = calcular_ganancia(datos)
    return jsonify({
        "ganancias_total": ganancias,
        "total_ventas": datos["total"],
        "promedio_venta": round(datos["promedio"], 2),
        "cantidad_registros": len(datos["ventas"])
    })


if __name__ == "__main__":
    app.run(debug=True)