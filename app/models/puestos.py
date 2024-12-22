# Importamos el objeto que hace referencia a la base de datos
from app.extensions import db

# Definimos la clase Usuario
class Puesto(db.Model):
    # Indicamos que la tabla se va a llamar 'usuarios'

    __tablename__ = 'puestos'# <-- indica a que tabla se va a referir  
    # Definimos los campos de la tabla
    id_puesto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Numeric(10,8), nullable=False,unique=True)
    longitude = db.Column(db.Numeric, nullable=False,unique=True)
    reseña = db.Column(db.Text(), nullable=False)
    foto_url = db.Column(db.Text(), nullable=False)
    calificacion_promedio = db.Column(db.Text(), nullable=False)
    
    def save(self):
        # crea una sesión en la base de datos
        db.session.add(self)
        # guarda los cambios en la base de datos y cierra la sesión
        db.session.commit()

    def delete(self):
        #abre una sesión en la base de datos
        db.session.delete(self)
        #guarda los cambios en la base de datos y cierra la sesión
        db.session.commit()