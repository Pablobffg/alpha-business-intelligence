import json
import os

class EvaluadorEstrategias:

    def __init__(self):
        self.archivo = "data/historial_estrategias.json"
        self.historial = self.cargar()

    def cargar(self):
        if not os.path.exists(self.archivo):
            return {}
        with open(self.archivo, "r") as f:
            return json.load(f)

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump(self.historial, f, indent=4)

    def registrar(self, estrategia, resultado):
        if estrategia not in self.historial:
            self.historial[estrategia] = []

        self.historial[estrategia].append(resultado)
        self.guardar()

    def evaluar(self):
        ranking = {}

        for estrategia, resultados in self.historial.items():
            score = sum(resultados) / len(resultados)
            ranking[estrategia] = score

        mejor = max(ranking, key=ranking.get)

        print("[EVALUADOR] Ranking:", ranking)
        print("[EVALUADOR] Mejor estrategia:", mejor)

        return mejor