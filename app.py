from flask import Flask, jsonify, request, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from data.lector_datos import cargar_datos, guardar_venta
from ia.prediccion import predecir_venta
from ia.simulador import simular_futuro
from ia.simulador_estrategia import simular_estrategias
from ia.finanzas import calcular_ganancia
from core.reporte_negocio import generar_reporte
import json
import os

app = Flask(__name__)
app.secret_key = "alpha_secret_key_2025"
CORS(app, supports_credentials=True)

USERS_FILE = "data/usuarios.json"

def cargar_usuarios():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def guardar_usuarios(usuarios):
    with open(USERS_FILE, "w") as f:
        json.dump(usuarios, f)


@app.route("/registro", methods=["POST"])
def registro():
    body = request.get_json()
    if not body or "usuario" not in body or "password" not in body:
        return jsonify({"error": "Faltan campos"}), 400

    usuarios = cargar_usuarios()
    if body["usuario"] in usuarios:
        return jsonify({"error": "Usuario ya existe"}), 400

    usuarios[body["usuario"]] = generate_password_hash(body["password"])
    guardar_usuarios(usuarios)
    return jsonify({"mensaje": "Usuario creado"})


@app.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    if not body or "usuario" not in body or "password" not in body:
        return jsonify({"error": "Faltan campos"}), 400

    usuarios = cargar_usuarios()
    if body["usuario"] not in usuarios:
        return jsonify({"error": "Usuario no encontrado"}), 401

    if not check_password_hash(usuarios[body["usuario"]], body["password"]):
        return jsonify({"error": "Contraseña incorrecta"}), 401

    session["usuario"] = body["usuario"]
    return jsonify({"mensaje": "Login exitoso", "usuario": body["usuario"]})


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("usuario", None)
    return jsonify({"mensaje": "Sesión cerrada"})


@app.route("/me", methods=["GET"])
def me():
    if "usuario" not in session:
        return jsonify({"error": "No autenticado"}), 401
    return jsonify({"usuario": session["usuario"]})


@app.route("/reporte", methods=["GET"])
def reporte():
    datos = cargar_datos()
    mejor = simular_estrategias(datos)
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


@app.route("/historial", methods=["GET"])
def historial():
    datos = cargar_datos()
    ventas = datos["ventas"]
    return jsonify({
        "ventas": ventas,
        "total_registros": len(ventas)
    })

@app.route("/historial/filtrado", methods=["GET"])
def historial_filtrado():
    desde = request.args.get("desde", None)
    hasta = request.args.get("hasta", None)
    datos = cargar_datos()
    ventas = datos["ventas"]
    
    # Por ahora filtramos por índice simulando fechas
    total = len(ventas)
    if desde and hasta:
        try:
            inicio = int(desde)
            fin = int(hasta)
            ventas = ventas[inicio:fin]
        except:
            pass
    
    return jsonify({
        "ventas": ventas,
        "total": sum(ventas),
        "promedio": round(sum(ventas)/len(ventas), 2) if ventas else 0,
        "total_registros": len(ventas)
    })
if __name__ == "__main__":
    app.run(debug=True)