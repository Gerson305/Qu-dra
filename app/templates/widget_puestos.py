# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget
from ui_widget_puestos import  Ui_puesto



class WidgetPuesto(QWidget):
    def __init__(self, nombre='',resenia='',parent=None):
        super().__init__(parent)

        self.ui = Ui_puesto()
        self.ui.setupUi(self)

        self.ui.widget_nombre.setText(nombre)
        self.ui.widget_resenia.setText(resenia)

# if __name__ == "__main__":
#     pass
