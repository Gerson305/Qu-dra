# Importamos el objeto que hace referencia a la base de datos
from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash

# Definimos la clase Usuario
class User(db.Model):
    # Indicamos que la tabla se va a llamar 'usuarios'

    __tablename__ = 'usuarios'# <-- indica a que tabla se va a referir  
    # Definimos los campos de la tabla
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    contrasenia = db.Column(db.Text(), nullable=False)

    # La contraseña que nos envia el usuario , llega a la funcion, que se envia a la BD
    def hashear_password(self, contrasenia):
        self.contrasenia = generate_password_hash(contrasenia)

    # Esta función recibre la contraseña en texto plano y la compara con el has almacenado
    def verificar_password(self, contrasenia):
        return check_password_hash(self.contrasenia, contrasenia)
    
    

# Método de la clase User para guardar un nuevo usuario en la base de datos 
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


# Método de la clase User para validar la contraseña del usuario

