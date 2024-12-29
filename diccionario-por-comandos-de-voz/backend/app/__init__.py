from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Cargar configuraciones
    app.config.from_object('backend.instance.config.Config')
    
    # Importar las rutas
    from .routes import main
    app.register_blueprint(main)
    
    return app