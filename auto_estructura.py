import os

nombre_proyecto = input("Nombre del proyecto: ")

estructura = [
    "data",
    "scripts",
    "docs",
    "models",
    "tests",
    "outputs"
]

ruta_base = os.path.join(os.getcwd(), nombre_proyecto)

os.mkdir(ruta_base)

for carpeta in estructura:
    os.mkdir(os.path.join(ruta_base, carpeta))

print(f"\nProyecto '{nombre_proyecto}' creado con estructura profesional.")