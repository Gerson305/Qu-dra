import requests # librería para consumir datos de internet
import json
import os
import jwt
import datetime
import asyncio
import httpx
import aiofiles

# This Python file uses the following encoding: utf-8
# esta es la url a la cual vamos a mandar la información
url = 'http://127.0.0.1:8081'
# Determine la caducidad de token
def eliminar_token():
    with open('token.txt','w') as file:
        # Dentro de ese archivo, se guarde el token
        file.write('')

def token_es_valido(expiracion):
    #Covierte Exp en fecha
    fecha_expiracion = datetime.datetime.fromtimestamp(expiracion)
    return fecha_expiracion > datetime.datetime.now()
    # si es mayor significa que  Válido True , si es menor token ya expiró false

# Una función para poder decodificar el token

def decode_token(token):
    # verificando si hay token para decodificar
    if token:
        #Decodificamos el payload del token
        payload = jwt.decode(token, options={'verify_signature':False})
        # imprimimos el payload
        return payload
    return None


#Cargar el archivo token.txt para obtenet Token
def cargar_token():

    # comprobar si existe el archivo
    if os.path.exists('token.txt'):
    # El archivo existe lo abrimos y retornamos el token
        with open ('token.txt', 'r') as file:
            contenido = file.read()
            # compara si el archivo donde se almacena el token esta vacio
            if len(contenido) == 0:
                return None

            return contenido
    else:
        return None

# Crear un archivo donde se almacena el token
async def crear_archivo_token(token):
    # Abra un archivo y si no existe, que lo cree
    async with aiofiles.open('token.txt','w') as file:
        # Dentro de ese archivo, se guarde el token
        await file.write(token)

# Esta función nos ayudará a crear usuarios y guardar en una BD
def registrar_usuario(nombre, apellido, correo, password):
    # El diccionario contendrá toda la información que se registrara en la DB
    informacion_a_enviar={
    'nombre':nombre + ' ' + apellido,    
    'correo': correo,
    'contrasenia': password
    }

    print(informacion_a_enviar)
    respuesta = requests.post(url+'/registro',data=informacion_a_enviar)
    respuesta_string = respuesta.content.decode('utf-8')
    respuesta_diccionario = json.loads(respuesta_string)


    return  respuesta_diccionario

async def login_usuario(correo,password):
    # Enviará toda la información
    informacion_a_enviar={
    'correo':correo,
    'contrasenia':password
    }
    print (informacion_a_enviar)


    # print(respuesta.content)

    async with httpx.AsyncClient() as cliente:
        respuesta = await cliente.post(url+'/login', data=informacion_a_enviar)

    respuesta_string = respuesta.content.decode('utf-8')
    respuesta_diccionario = json.loads(respuesta_string)

    if 'Token' in respuesta_diccionario:
        # se crea el archivo "token.txt"
        await crear_archivo_token(respuesta_diccionario['Token'])

    return respuesta_diccionario

if __name__ == "__main__":
    mi_token_actual = cargar_token()
    print (mi_token_actual)
    payload_token = decode_token(mi_token_actual)

    valido = token_es_valido(payload_token['exp'])
    print(valido)
#     #pass
