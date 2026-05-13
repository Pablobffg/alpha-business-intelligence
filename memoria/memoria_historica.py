import json
import os

ARCHIVO_MEMORIA = "memoria/historial.json"

def guardar_registro(datos, decision):

    registro = {
        "ventas": datos.get("total", 0),
        "promedio": datos.get("promedio", 0),
        "decision": decision
    }

    historial = []

    if os.path.exists(ARCHIVO_MEMORIA):
        with open(ARCHIVO_MEMORIA, "r") as f:
            historial = json.load(f)

    historial.append(registro)

    with open(ARCHIVO_MEMORIA, "w") as f:
        json.dump(historial, f, indent=4)

    print("[MEMORIA] Registro guardado en historial")