# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Card_widget(object):
    def setupUi(self, Card_widget):
        if not Card_widget.objectName():
            Card_widget.setObjectName(u"Card_widget")
        Card_widget.resize(200, 288)
        Card_widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.horizontalLayout = QHBoxLayout(Card_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_Card_widget = QFrame(Card_widget)
        self.frame_Card_widget.setObjectName(u"frame_Card_widget")
        self.frame_Card_widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_Card_widget.setFrameShape(QFrame.StyledPanel)
        self.frame_Card_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Card_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.But_Card_widget = QPushButton(self.frame_Card_widget)
        self.But_Card_widget.setObjectName(u"But_Card_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.But_Card_widget.sizePolicy().hasHeightForWidth())
        self.But_Card_widget.setSizePolicy(sizePolicy)
        self.But_Card_widget.setMinimumSize(QSize(162, 250))
        self.But_Card_widget.setMaximumSize(QSize(162, 250))
        self.But_Card_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.But_Card_widget.setStyleSheet(u"background-color: rgb(230, 230, 230, 90);\n"
"border-radius:10px\n"
"\n"
"")

        self.verticalLayout.addWidget(self.But_Card_widget)


        self.horizontalLayout.addWidget(self.frame_Card_widget)


        self.retranslateUi(Card_widget)

        QMetaObject.connectSlotsByName(Card_widget)
    # setupUi

    def retranslateUi(self, Card_widget):
        Card_widget.setWindowTitle(QCoreApplication.translate("Card_widget", u"Form", None))
        self.But_Card_widget.setText("")
    # retranslateUi

