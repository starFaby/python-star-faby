from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .database import db

def createApp():
    """Metodo para la creacion de la app flask"""
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config) # para que el metodo sea la conexion exitosa

    db.init_app(app)
    return app