import os

# Definir la estructura del proyecto
estructura = {
    "diccionario-por-comandos-de-voz": {
        "backend": {
            "app": [
                "__init__.py",
                "routes.py",
                "models.py",
                "config.py"
            ],
            "instance": [
                "config.py"
            ],
            "templates": [
                "index.html",
                "agregar_palabra.html"
            ],
            "static": {
                "css": [
                    "styles.css"
                ]
            },
            "run.py": None  # Esto es para indicar que el archivo `run.py` debe ser creado.
        }
    }
}


# Función para crear las carpetas y archivos
def crear_estructura(base_path, estructura):
    for nombre, contenido in estructura.items():
        path = os.path.join(base_path, nombre)
        
        if isinstance(contenido, dict):
            # Si es un diccionario, crear la carpeta y procesar sus subcarpetas
            os.makedirs(path, exist_ok=True)
            crear_estructura(path, contenido)
        elif isinstance(contenido, list):
            # Si es una lista, crear los archivos dentro de la carpeta
            os.makedirs(path, exist_ok=True)
            for archivo in contenido:
                archivo_path = os.path.join(path, archivo)
                with open(archivo_path, 'w') as f:
                    pass  # Crear archivo vacío
        else:
            # Crear archivo vacío directamente si no hay más subcarpetas o listas
            with open(path, 'w') as f:
                pass  # Crear archivo vacío

# Crear la estructura en la ruta actual
crear_estructura('.', estructura)
