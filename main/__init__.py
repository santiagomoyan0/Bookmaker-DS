import os
from flask import Flask

from dotenv import load_dotenv

# Importar librería flask_restful
from flask_restful import Api
# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Importar Flask JWT

api = Api()
# Inicializar SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.mknod(f'{PATH}{DB_NAME}')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{PATH}{DB_NAME}'
    db.init_app(app)
    



    # Importar directorio de recursos
    import main.controlers as controlers
    api.add_resource(controlers.ClienteControlers, '/clientes')
    api.add_resource(controlers.ClienteControlers, '/cliente/<id>')
    api.add_resource(controlers.EmpresasControlers, '/empresas')
    api.add_resource(controlers.EmpresaControlers, '/empresa/<id>')
    api.add_resource(controlers.EquiposControlers, '/equipos')
    api.add_resource(controlers.EquipoControlers, '/equipo/<id>')

    
    # Cargar la aplicación en la API de Flask Restful
    api.init_app(app)
    return app