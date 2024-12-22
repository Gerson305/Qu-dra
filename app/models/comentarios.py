# Importamos el objeto que hace referencia a la base de datos
from app.extensions import db

# Definimos la clase Usuario
class comentarios(db.Model):
    # Indicamos que la tabla se va a llamar 'usuarios'

    __tablename__ = 'comentarios'# <-- indica a que tabla se va a referir  
    # Definimos los campos de la tabla
    id_comentario = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_puesto = db.Column(db.Integer, db.ForeignKey('puestos.id_puesto'), nullable=False)
    contenido = db.Column(db.Text(), nullable=False)

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
    