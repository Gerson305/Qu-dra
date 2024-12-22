# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from widget_puestos import  WidgetPuesto


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Pagina_principal
from ventana_emergente import VentanaEmergente
# clase para cambiar de ventanas
from router import  RouterManager
from metodos import cargar_token
from metodos import decode_token
from metodos import token_es_valido
from metodos import eliminar_token

from qasync import QEventLoop
import asyncio

class Pagina_principal(QMainWindow):
    def __init__(self,nombre_usuario="", parent=None):
        super().__init__(parent)

        # Tenemos un atributo importante hace referencia de donde obtiene la parte gráfica
        self.ui = Ui_Pagina_principal()

        # Atributo que almacene el nombre del usuario
        self.nombre_usuario = nombre_usuario

        # de ese apartado gráfico lo inicializamos
        self.ui.setupUi(self)
        # creamos un objeto de tipo RouterManager
        self.router_manager = RouterManager()
        # Creamos un espacio donde vamos a poner todas las tareas layout

        self.layout_puestos = QHBoxLayout()
        self.ui.contenedor_puestos.setLayout(self.layout_puestos)
        self.ui.label_2.setText(f'Bienvenid@  {self.nombre_usuario}')
        self.ui.cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.ui.agregar_puesto.clicked.connect(self.abrir_ventana_emergente)




    def abrir_ventana_emergente(self):
        # se crea un atributo del objeto VentanaEmergente
        self.ventana = VentanaEmergente(self)
        # Se intercepta la señal emitida
        self.ventana.datos_a_enviar.connect(self.aceptar_datos)

        # Mostrar la ventana
        self.ventana.exec()

    def aceptar_datos(self,datos):
        print(f'Información interceptada:{datos}')
        nuevo_puesto = WidgetPuesto(nombre=datos[0],resenia=datos[1])
        self.layout_puestos.addWidget(nuevo_puesto)


    def cerrar_sesion(self):
        eliminar_token()
        # esta línea nos ayuda a enviar al usuario a login
        self.router_manager.acceder_login(ventana_anterior=self)



# Determinar si el usuario esta ejecutando este archivo
if __name__ == "__main__":

    # tenemos que determinar el estado del Token
    token_actual = cargar_token()

    # decodificamos
    payload_token = decode_token(token_actual)

    if payload_token:
        valido = token_es_valido(payload_token['exp'])
    else:
        valido = None


    router_manager = RouterManager()

    # Primero creamos una aplicación
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    # crear el entorno asíncrono para nuestra app
    asyncio.set_event_loop(loop)

    #Creamos la vista de la aplicación
    widget = Pagina_principal()

    # Mostramos la aplicación
    #widget.show()


    if valido:
        # si el token en valido el admin de rutas hace acceder al usuario a la página principal
        print('Se cargar la pagina inicio')
        nombre = payload_token['sub']
        router_manager.acceder_principal(widget, nombre)

    else:
        # Sí el token es inválido el admin de rutas envía al usuario a la página login
        print('Se carga login')
        router_manager.acceder_login(widget)

    with loop:
        loop.run_forever()
   #Sale de la app si se preciona en la ventana X
    sys.exit(app.exec())
