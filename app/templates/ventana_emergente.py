# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from ui_ventana_emergente import Ui_ventana_emergente


class VentanaEmergente(QDialog):
    #Señal que llega a la ventana principal en forma de lista
    datos_a_enviar = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ventana_emergente()

        self.ui.setupUi(self)



        #conectar los botones
        self.ui.botones_ventana.accepted.connect(self.enviar_datos)
    def enviar_datos(self):
        nombre = self.ui.nombre_puesto.text()
        resenia = self.ui.Resenia.toPlainText()

        datos = [nombre, resenia]

        self.datos_a_enviar.emit(datos)
        self.accept()




# if __name__ == "__main__":
#     pass
