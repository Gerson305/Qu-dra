# This Python file uses the following encoding: utf-8
import sys #  <- Nos ayuda a controlar sistema(Cuando el usuario desee salir)

# importar para crear componentes de QT
from PySide6.QtWidgets import QApplication, QMainWindow

# desde el archivo registro.ui importar el componente
from ui_registro import Ui_Pagina_registro
from router import RouterManager
from metodos import registrar_usuario
# hasta aquí se completa la importación
#------------------------------------------------------
class PaginaRegistro(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.router_manager = RouterManager()

      # indicamos de donde se obtendra la parte visual
        self.ui = Ui_Pagina_registro()
      # inicializamos
        self.ui.setupUi(self)
        # si el usuario presiona el boton registro validamos
        self.ui.registrar.clicked.connect(self.validar_datos)
        # si el usuario presiona el boton
        self.ui.inicio_sesion.clicked.connect(self.mandar_login)

#_______________________________________________________
# Obtenemos toda la información que el usuario envia
    def validar_datos(self):
        nombre = self.ui.texto_nombre.text()
        apellidos = self.ui.texto_apellidos.text()        
        correo = self.ui.texto_correo.text()
        password_1 = self.ui.password_1.text()
        password_2 = self.ui.password_2.text()

# 1.- Asegurarnos que ningún parámetro este vacío
# 1.1.- Si alguno viene vacío, tenemos que generar un error
        if (len(nombre) <= 0) or (len(apellidos) <=0 ) or (len(password_1) <= 0):
            print ('Error : Datos faltantes')
            self.ui.error.setText('Error :( Datos faltantes')
#2.- El correo que ingrese el usuario se válido
#2.2.- Si no es válido, generamos un error

        elif '@' not in correo and '.' not in correo:
            self.ui.error.setText('Ingresa un correo valido')
#3.- Que ambas contraseñas coincidan
#3.3.- Si alguna de las contraseñas no coincide tenemos que generar un error
        elif password_1 != password_2:
            self.ui.error.setText('Error: Las contraseñas no coinciden :(')
# Si toda la información es válida guardadmos en DB y  enviamos a login
        else:
            print ('Datos Validados')
            self.ui.error.setText('')

            resultado = registrar_usuario(nombre, apellidos, correo, password_1)
            # si se cumple tenemos un usuario ya registrado
            if 'Error' in resultado:
                self.ui.error.setText('Este correo  ya está asociado a otra cuenta')
            else:
                # Sí la información es váliada se guarda en DB y se manda a login
                self.mandar_login()

    def mandar_login(self):
        self.router_manager.acceder_login(self)


if __name__ == "__main__":
    # Primero creamos una aplicación
    app = QApplication(sys.argv)
    # Creamos la vista de la aplicación
    widget = PaginaRegistro()
    # Mostramos la aplicación
    widget.show()
    #Sale de la app si se preciona en la ventana X
    sys.exit(app.exec())
