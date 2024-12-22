# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QMovie,QPixmap
from ui_login import Ui_LoginWindow
from router import RouterManager
from metodos import login_usuario
from metodos import cargar_token
from metodos import decode_token
import asyncio
from qasync import  asyncSlot


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Inicializamos un par de atribútos
        # Contrandra la UI de nuestra ventana
        self.ui = Ui_LoginWindow()
        # Configurar la ventana que vamos a mostrar
        self.ui.setupUi(self)
        self.router_manager = RouterManager()

        #Se crea un atributo que defina un objeto Qmovie
        self.spinner_loading = QMovie('loading-gif.gif')
        self.ui.cargando.setMovie(self.spinner_loading)
        self.spinner_loading.stop()
        self.spinner_loading.setScaledSize(self.ui.cargando.size())
        self.ui.cargando.hide()

        # cuando el botón registro sea presionado ejecutamos mandar a registro
        self.ui.registro.clicked.connect(self.mandar_a_registro)

        # Cuando el botón iniciamos sesión
        self.ui.iniciar_sesion.clicked.connect(self.manejar_inicio_asincrono)

# Este método redirige al usuario a la ventana de registro
    def mandar_a_registro(self):
        self.router_manager.acceder_registro(ventana_anterior=self)


    # Este manejador nos permite utilizar funciones asíncronas
    @asyncSlot()
    async def manejar_inicio_asincrono(self):
        await self.iniciar_sesion()
# Inicia sesión y manda al usuario a la pagina principal
    async def iniciar_sesion(self):

        correo = self.ui.Correo.text()
        password = self.ui.password.text()
        #self.ui.cargando.setText('Cargando...') Iniciar sesión se muestra Gif
        self.ui.cargando.show()
        self.spinner_loading.start()
        respuesta = await login_usuario(correo,password)
        print (respuesta)
        #self.ui.cargando.setText('') Cuando termina de cargar se esconde Gif
        self.spinner_loading.stop()
        self.ui.cargando.hide()
        mi_token = cargar_token()
        #print (f'el token en este punto es:{mi_token}')
        datos_token = decode_token(mi_token)

        print (respuesta)

        if 'Token' in respuesta:
            self.router_manager.acceder_principal(self,datos_token['sub'])
        else:
            self.ui.error.setText(respuesta['Status'])
        #if correo == 'admin@correo.com' and password == '123':

        #else:
         #   self.ui.error.setText('El correo o la contraseña no coinciden :(')

# nos ayuda a depurar
if __name__ == "__main__":
    app = QApplication(sys.argv)  # nos ayuda a que se detecten las acciones del usuario

    # creamos un objeto que va a contener nuestra ventana
    widget =LoginWindow()

    widget.show()

    # detecta si el usuario quiere salir X
    sys.exit(app.exec())


#     pass
