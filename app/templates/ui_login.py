# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(660, 464)
        palette = QPalette()
        brush = QBrush(QColor(213, 208, 155, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        LoginWindow.setPalette(palette)
        LoginWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 361, 81))
        self.label.setStyleSheet(u"font: 48pt \"Franklin Gothic Demi Cond\";\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 140, 58, 19))
        self.Correo = QLineEdit(self.centralwidget)
        self.Correo.setObjectName(u"Correo")
        self.Correo.setGeometry(QRect(80, 160, 301, 24))
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(80, 220, 301, 24))
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 200, 81, 19))
        self.iniciar_sesion = QPushButton(self.centralwidget)
        self.iniciar_sesion.setObjectName(u"iniciar_sesion")
        self.iniciar_sesion.setGeometry(QRect(170, 280, 121, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 340, 131, 19))
        self.registro = QPushButton(self.centralwidget)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(90, 360, 84, 31))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(80, 260, 311, 20))
        self.error.setStyleSheet(u"color:rgb(170, 0, 0)")
        self.cargando = QLabel(self.centralwidget)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(240, 320, 30, 30))
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setGeometry(QRect(430, 20, 211, 201))
        self.logo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.logo.setAutoFillBackground(False)
        self.logo.setPixmap(QPixmap(u"logo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(True)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 25))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Qu@dr@", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700;\">Ingreso Qu@dr@</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.iniciar_sesion.setText(QCoreApplication.translate("LoginWindow", u"Iniciar sesi\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"\u00bfNo tienes cuenta?", None))
        self.registro.setText(QCoreApplication.translate("LoginWindow", u"Crea una", None))
        self.error.setText("")
        self.cargando.setText("")
        self.logo.setText("")
    # retranslateUi

