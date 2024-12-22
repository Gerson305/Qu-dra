# se va a encargar de montar el servidor 
# flask libreria y Flask es el módulo
from flask import Flask  # permite crear el servidor
from flask_restful import Api # Crear la funcionalidad de API
#Importar un archivo 
from .routes import APIRoutes
# Creamos una funcion que configure el servidor
# importamos la clase config desde el archivo config.py que establece la uri de la base de datos
from .config import Config
# importamos de el archivo extensions.py la clase db  que instancia el objeto db
from .extensions import db,jwt
# Importamos para acceso con token
from  flask_jwt_extended.exceptions import NoAuthorizationError,InvalidHeaderError
from flask import jsonify # convertir a JSON


def configurar_app():
    # Variable para almacenar el servidor
    app = Flask(__name__)

    # Le indico a la app que va a usar la configuración de la clase Config
    app.config.from_object(Config)
    # Le indico a la db que se va a inicializar con la app
    db.init_app(app)
    # Miestras el servidor se esta montando, se va a crear la base de datos
# JWT se va a inicializar
    jwt.init_app(app)

    with app.app_context():
        # Crea todas las tablas
        db.create_all()
    # indicamos sobre que servidor va a interactuar
    api = Api(app)

    # Configuramos las rutas y los recursos
    rutas= APIRoutes()
    rutas.init_api(api)

    # Se ejecuta la función cuando se lanza el decorador 
    @app.errorhandler(NoAuthorizationError)
    def manejar_no_token(error):
        return jsonify({
            'Mensaje':'Necesitas un Token para acceder',
            'Error': str(error)
        }, 401)
    # Se ejecuta la función cuando se lanza el decorador
    @app.errorhandler(InvalidHeaderError)
    def manejar_token_invalido(error):
        return jsonify({
            'Mensaje':'Token invalido o mal formado',
            'Error': str(error)
        }, 422)
    @jwt.expired_token_loader
    def manejar_token_expirado(jwt_header, jwt_payload):
        return jsonify ({
            'Mensaje':'El token ya expiro',
            'Error': 'token expirado'
        }, 401)

    return app




