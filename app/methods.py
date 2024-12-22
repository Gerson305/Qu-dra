# ejecuta todas las peticiones que se hagan a la DB
from app.models.usuarios import User
from app.models.puestos import Puesto
from app.models.comentarios import comentarios
from app.models.calificaciones import calificaciones
from flask_jwt_extended import create_access_token

from datetime import timedelta 

def user_register(nombre, correo, contrasenia):
    # buscar si el correo del usuario ya esta registrado
    usuario_existente = User.query.filter_by(correo=correo).first()

    if usuario_existente is not None:
        return {'Error': 'El usuario ya está registrado :('}, 403
    
    #creamos un objeto de tipo User con los datos que el usuario nos proporciona
    nuevo_usuario = User(nombre=nombre, correo=correo, contrasenia=contrasenia)
    
    # Este método recibe el pass en texto plano, hashea y guarda en has en el objeto
    nuevo_usuario.hashear_password(contrasenia=contrasenia)

    #guardamos el nuevo usuario en la base de datos
    nuevo_usuario.save()

    return {
        'status': 'Usuario registrado',
        'correo' : correo,
        'nombre' : nombre
    }, 200
def puesto_register(nombre, latitude, longitude, reseña, foto_url, calificacion_promedio):
    # buscar si la ubicación del puesto ya esta registrada
    puesto_existente = Puesto.query.filter_by(latitude=latitude).first()
   
    if puesto_existente is not None:
        return {'Error': 'La ubicación del puesto ya esta registrada  :('}, 403
    
    #creamos un objeto de tipo puesto con los datos que el usuario nos proporciona
    nuevo_puesto = Puesto(nombre=nombre, latitude=latitude,longitude=longitude,reseña=reseña,foto_url=foto_url,calificacion_promedio=calificacion_promedio)
    
    nuevo_puesto.save() 

    return {
        'status': 'Puesto registrado',
        'nombre' : nombre,
        'latitude' : latitude,
        'longitude' : longitude,
        'reseña' : reseña,
        'foto_url': foto_url,
        'calificacion_promedio' : calificacion_promedio

    }, 200
# esta funcion se encarga de hacer el login en nuestra API
def user_login(correo, contrasenia):

    # Tenemos que verificar que el usuario al que se esta intentando logear existe
    # En La DB se buscar por correo que el cliente manso
    usuario_existente = User.query.filter_by(correo=correo).first()
    # esta condición determina si el usuario esta registrado
    if usuario_existente is None:
        # si El correo no esta en DB manda un error
        return {'Status': 'El correo no está registrado :('}, 500
    # verificamos que la contraseña coincida con la de la DB
    elif usuario_existente.verificar_password(contrasenia=contrasenia):
        
        caducidad = timedelta(minutes=2)

        token_acceso = create_access_token (identity= usuario_existente.nombre , expires_delta=caducidad)
        print(token_acceso)
        return {'Status':'Sesión iniciada',
                'Token':token_acceso}, 200
    else:
        return {'Status':'La contraseña no coincide :('},400
    

    