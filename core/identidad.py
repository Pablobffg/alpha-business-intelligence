# core/identidad.py

class IdentidadSistema:
    def __init__(self):
        self.nombre = "WistexAI"
        self.version = "1.0"
        self.nivel_evolutivo = 1
        self.estado_actual = "operacion_normal"
        self.objetivos_globales = {
            "crecimiento": True,
            "estabilidad": True,
            "expansion": True,
            "optimizacion": True
        }

    def actualizar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado
        print(f"[IDENTIDAD] Estado actualizado a: {self.estado_actual}")

    def evolucionar(self):
        self.nivel_evolutivo += 1
        print(f"[IDENTIDAD] Nivel evolutivo aumentado a: {self.nivel_evolutivo}")

    def resumen(self):
        return {
            "nombre": self.nombre,
            "version": self.version,
            "nivel": self.nivel_evolutivo,
            "estado": self.estado_actual,
            "objetivos": self.objetivos_globales
        }