
from flask_restful import Resource
from flask import request, render_template, make_response #<- Nos permite interceptar la info del usuario
from app.methods import user_register
from app.methods import puesto_register
from app.methods import user_login
# si esta logeado o no
from flask_jwt_extended import jwt_required

# Creamos un recurso que nuestra aplicación puede cargar (METODO)
class HolaMundo(Resource):
  # Este método se ejecuta cuando el usuario lo llama con un GET
  def get(self):
    pagina = render_template('index.html')
    respuesta = make_response(pagina)
    #return {'Mensaje': 'Hola mundo desde GET'}
    return respuesta

  def post(self):
    return {'Mensaje': 'Hola mundo desde POST'}

class Registro(Resource):
  # Como el usuario envia información utilizamos un post
  def post(self):
    # Información que el usario envia a través del post
    user_info = request.form
    username = user_info.get('nombre')
    correo = user_info.get('correo')
    contrasenia = user_info.get('contrasenia')    

    respuesta, status = user_register(username, correo, contrasenia)
    
    return respuesta, status
  
class Puesto(Resource):
  # Como el usuario envia información utilizamos un post
    def post(self):
      # Información que el usario envia a través del post
      user_info = request.form
      nombre = user_info.get('nombre')
      latitude = user_info.get('latitude')
      longitude = user_info.get('longitude')
      reseña = user_info.get('reseña')
      foto_url = user_info.get('foto_url')
      calificacion_promedio = user_info.get('calificacion_promedio')

      respuesta, status = puesto_register(nombre, latitude, longitude,reseña,foto_url,calificacion_promedio)
      
      return respuesta, status


# Van a crear un recurso para el login, le van a asigar una ruta y su servidor tiene que recibir
# la siguiente información del cliente: "correo" y "contraseña"
class Login(Resource):

  def get(self):
    pagina = render_template('login.html')
    respuesta = make_response(pagina)
    return respuesta
  # Como el usuario envia información utilizamos un post
  def post(self):
    # Información que el usario envia a través del post
    user_info = request.form
    correo = user_info.get('correo')
    contrasenia = user_info.get('contrasenia')    
    respuesta, status = user_login(correo, contrasenia)
    return respuesta, status

# un recurso que se ejecuta cuando el usuario accede a la ruta /restringido
class Restringido(Resource):

  @jwt_required () # Verificamos si el usuario esta autorizado
  def get(self):
    #return{'Mensaje':'Felicidades estás loggeado'}
    pagina = render_template('restringido.html')
    respuesta = make_response(pagina)
    return respuesta
 

# Simplemente se va a encargar de darle rutas a mis recursos
class APIRoutes:
  def init_api(self, api):
    api.add_resource(HolaMundo, '/')
    api.add_resource(Registro, '/registro')
    api.add_resource(Login, '/login')
    api.add_resource(Restringido,'/restringido')
    api.add_resource(Puesto,'/puesto')