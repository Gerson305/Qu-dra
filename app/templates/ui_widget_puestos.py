# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_puestos.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_puesto(object):
    def setupUi(self, puesto):
        if not puesto.objectName():
            puesto.setObjectName(u"puesto")
        puesto.resize(686, 170)
        self.widget_nombre = QLabel(puesto)
        self.widget_nombre.setObjectName(u"widget_nombre")
        self.widget_nombre.setGeometry(QRect(20, 20, 58, 19))
        self.widget_resenia = QLabel(puesto)
        self.widget_resenia.setObjectName(u"widget_resenia")
        self.widget_resenia.setGeometry(QRect(20, 90, 81, 19))
        self.label_3 = QLabel(puesto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 0, 58, 19))
        self.pushButton = QPushButton(puesto)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 30, 84, 27))
        self.pushButton_2 = QPushButton(puesto)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 70, 84, 27))
        self.pushButton_3 = QPushButton(puesto)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 110, 84, 27))

        self.retranslateUi(puesto)

        QMetaObject.connectSlotsByName(puesto)
    # setupUi

    def retranslateUi(self, puesto):
        puesto.setWindowTitle(QCoreApplication.translate("puesto", u"Form", None))
        self.widget_nombre.setText(QCoreApplication.translate("puesto", u"Titulo", None))
        self.widget_resenia.setText(QCoreApplication.translate("puesto", u"Descripci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("puesto", u"Estado", None))
        self.pushButton.setText(QCoreApplication.translate("puesto", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("puesto", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("puesto", u"PushButton", None))
    # retranslateUi

