# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_emergente.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QWidget)

class Ui_ventana_emergente(object):
    def setupUi(self, ventana_emergente):
        if not ventana_emergente.objectName():
            ventana_emergente.setObjectName(u"ventana_emergente")
        ventana_emergente.resize(550, 394)
        self.botones_ventana = QDialogButtonBox(ventana_emergente)
        self.botones_ventana.setObjectName(u"botones_ventana")
        self.botones_ventana.setGeometry(QRect(120, 350, 391, 32))
        self.botones_ventana.setOrientation(Qt.Orientation.Horizontal)
        self.botones_ventana.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(ventana_emergente)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 141, 19))
        self.label_2 = QLabel(ventana_emergente)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 58, 19))
        self.nombre_puesto = QLineEdit(ventana_emergente)
        self.nombre_puesto.setObjectName(u"nombre_puesto")
        self.nombre_puesto.setGeometry(QRect(40, 70, 471, 31))
        self.Resenia = QTextEdit(ventana_emergente)
        self.Resenia.setObjectName(u"Resenia")
        self.Resenia.setGeometry(QRect(40, 140, 471, 191))

        self.retranslateUi(ventana_emergente)
        self.botones_ventana.accepted.connect(ventana_emergente.accept)
        self.botones_ventana.rejected.connect(ventana_emergente.reject)

        QMetaObject.connectSlotsByName(ventana_emergente)
    # setupUi

    def retranslateUi(self, ventana_emergente):
        ventana_emergente.setWindowTitle(QCoreApplication.translate("ventana_emergente", u"Agregar Puesto", None))
        self.label.setText(QCoreApplication.translate("ventana_emergente", u"Nombre del puesto", None))
        self.label_2.setText(QCoreApplication.translate("ventana_emergente", u"Rese\u00f1a", None))
    # retranslateUi

