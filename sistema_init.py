import os

nombre = input("Nombre del proyecto: ")

carpetas = {
    "data": ["dataset.csv"],
    "scripts": ["main.py", "utils.py"],
    "docs": ["readme.md"],
    "models": ["model.py"],
    "tests": ["test_main.py"],
    "outputs": ["resultados.txt"]
}

ruta = os.path.join(os.getcwd(), nombre)
os.mkdir(ruta)

for carpeta, archivos in carpetas.items():
    ruta_carpeta = os.path.join(ruta, carpeta)
    os.mkdir(ruta_carpeta)
    for archivo in archivos:
        with open(os.path.join(ruta_carpeta, archivo), "w") as f:
            f.write(f"# {archivo} creado automáticamente\n")

print("Sistema de proyecto inteligente creado.")