# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_Pagina_principal(object):
    def setupUi(self, Pagina_principal):
        if not Pagina_principal.objectName():
            Pagina_principal.setObjectName(u"Pagina_principal")
        Pagina_principal.resize(579, 465)
        self.centralwidget = QWidget(Pagina_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 40, 311, 51))
        font = QFont()
        font.setFamilies([u"Microsoft PhagsPa"])
        font.setPointSize(23)
        self.label.setFont(font)
        self.cerrar_sesion = QPushButton(self.centralwidget)
        self.cerrar_sesion.setObjectName(u"cerrar_sesion")
        self.cerrar_sesion.setGeometry(QRect(410, 420, 121, 21))
        self.cerrar_sesion.setMaximumSize(QSize(16777215, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.cerrar_sesion.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 541, 31))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.agregar_puesto = QPushButton(self.centralwidget)
        self.agregar_puesto.setObjectName(u"agregar_puesto")
        self.agregar_puesto.setGeometry(QRect(20, 100, 131, 27))
        self.contenedor_puestos = QScrollArea(self.centralwidget)
        self.contenedor_puestos.setObjectName(u"contenedor_puestos")
        self.contenedor_puestos.setGeometry(QRect(20, 140, 541, 271))
        self.contenedor_puestos.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 539, 269))
        self.contenedor_puestos.setWidget(self.scrollAreaWidgetContents)
        Pagina_principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pagina_principal)

        QMetaObject.connectSlotsByName(Pagina_principal)
    # setupUi

    def retranslateUi(self, Pagina_principal):
        Pagina_principal.setWindowTitle(QCoreApplication.translate("Pagina_principal", u"Pagina_principal", None))
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("Pagina_principal", u"<html><head/><body><p>Principal</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Pagina_principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20 pt; font-weight:700; color:#3d3d3d;\">Mapa de puestos</span></p></body></html>", None))
        self.cerrar_sesion.setText(QCoreApplication.translate("Pagina_principal", u"Cerrar Sesi\u00f3n", None))
        self.label_2.setText("")
        self.agregar_puesto.setText(QCoreApplication.translate("Pagina_principal", u"Agregar Puesto ", None))
    # retranslateUi

