# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Pagina_registro(object):
    def setupUi(self, Pagina_registro):
        if not Pagina_registro.objectName():
            Pagina_registro.setObjectName(u"Pagina_registro")
        Pagina_registro.resize(525, 600)
        self.centralwidget = QWidget(Pagina_registro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 71, 19))
        self.texto_nombre = QLineEdit(self.centralwidget)
        self.texto_nombre.setObjectName(u"texto_nombre")
        self.texto_nombre.setGeometry(QRect(130, 110, 291, 24))
        self.texto_apellidos = QLineEdit(self.centralwidget)
        self.texto_apellidos.setObjectName(u"texto_apellidos")
        self.texto_apellidos.setGeometry(QRect(130, 170, 291, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 150, 58, 19))
        self.texto_correo = QLineEdit(self.centralwidget)
        self.texto_correo.setObjectName(u"texto_correo")
        self.texto_correo.setGeometry(QRect(130, 220, 291, 24))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 200, 58, 19))
        self.password_1 = QLineEdit(self.centralwidget)
        self.password_1.setObjectName(u"password_1")
        self.password_1.setGeometry(QRect(130, 280, 291, 24))
        self.password_1.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 250, 81, 19))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 310, 141, 19))
        self.password_2 = QLineEdit(self.centralwidget)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(130, 340, 291, 24))
        self.password_2.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.registrar = QPushButton(self.centralwidget)
        self.registrar.setObjectName(u"registrar")
        self.registrar.setGeometry(QRect(210, 430, 131, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 480, 141, 19))
        self.inicio_sesion = QPushButton(self.centralwidget)
        self.inicio_sesion.setObjectName(u"inicio_sesion")
        self.inicio_sesion.setGeometry(QRect(230, 510, 101, 27))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(260, 540, 261, 19))
        self.error.setStyleSheet(u"font: 10pt \"Tw Cen MT Condensed Extra Bold\";color:rgb(170, 0, 0);\n"
"")
        Pagina_registro.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Pagina_registro)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 525, 25))
        Pagina_registro.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Pagina_registro)
        self.statusbar.setObjectName(u"statusbar")
        Pagina_registro.setStatusBar(self.statusbar)

        self.retranslateUi(Pagina_registro)

        QMetaObject.connectSlotsByName(Pagina_registro)
    # setupUi

    def retranslateUi(self, Pagina_registro):
        Pagina_registro.setWindowTitle(QCoreApplication.translate("Pagina_registro", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Pagina_registro", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Registro</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Pagina_registro", u"Nombre(s)", None))
        self.label_4.setText(QCoreApplication.translate("Pagina_registro", u"Apellidos", None))
        self.texto_correo.setText("")
        self.label_6.setText(QCoreApplication.translate("Pagina_registro", u"Correo", None))
        self.password_1.setText("")
        self.label_7.setText(QCoreApplication.translate("Pagina_registro", u"Contrase\u00f1a", None))
        self.label_8.setText(QCoreApplication.translate("Pagina_registro", u"Verificar contrase\u00f1a", None))
        self.password_2.setText("")
        self.registrar.setText(QCoreApplication.translate("Pagina_registro", u"Registrarme", None))
        self.label_3.setText(QCoreApplication.translate("Pagina_registro", u"\u00bfYa tienes una cuenta?", None))
        self.inicio_sesion.setText(QCoreApplication.translate("Pagina_registro", u"Iniciar sesi\u00f3n", None))
        self.error.setText(QCoreApplication.translate("Pagina_registro", u"<html><head/><body><p><span style=\" color:#ff5500;\"><br/></span></p></body></html>", None))
    # retranslateUi

