from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
# instancia llamada db la cual nos permite interacturar con la base de datos
db = SQLAlchemy()
# Creamos una clase jwt que nos ayudara a manajar todos los toquen que pasen por nuestra API
jwt = JWTManager()