# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardWindowUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import resCardWindow_rc

class Ui_Card_Window(object):
    def setupUi(self, Card_Window):
        if not Card_Window.objectName():
            Card_Window.setObjectName(u"Card_Window")
        Card_Window.resize(470, 431)
        Card_Window.setMinimumSize(QSize(470, 431))
        Card_Window.setMaximumSize(QSize(470, 431))
        Card_Window.setStyleSheet(u"background-color: rgb(253, 253, 253);")
        self.verticalLayout = QVBoxLayout(Card_Window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_for_buttons = QFrame(Card_Window)
        self.frame_for_buttons.setObjectName(u"frame_for_buttons")
        self.frame_for_buttons.setMinimumSize(QSize(0, 36))
        self.frame_for_buttons.setMaximumSize(QSize(16777215, 36))
        self.frame_for_buttons.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_for_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_for_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_for_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Layout_buttons = QHBoxLayout()
        self.Layout_buttons.setObjectName(u"Layout_buttons")
        self.But_flag = QPushButton(self.frame_for_buttons)
        self.But_flag.setObjectName(u"But_flag")
        self.But_flag.setMinimumSize(QSize(60, 18))
        self.But_flag.setMaximumSize(QSize(60, 18))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        font.setBold(True)
        self.But_flag.setFont(font)
        self.But_flag.setStyleSheet(u"QPushButton {\n"
"color: rgb(90, 90, 90);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(210, 210, 210, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/for_app_ui_card/icons8-\u043e\u043a-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_flag.setIcon(icon)

        self.Layout_buttons.addWidget(self.But_flag)

        self.But_edit = QPushButton(self.frame_for_buttons)
        self.But_edit.setObjectName(u"But_edit")
        self.But_edit.setMinimumSize(QSize(60, 18))
        self.But_edit.setMaximumSize(QSize(60, 18))
        self.But_edit.setFont(font)
        self.But_edit.setStyleSheet(u"QPushButton {\n"
"color: rgb(90, 90, 90);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(210, 210, 210, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/for_app_ui_card/icons8-\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_edit.setIcon(icon1)

        self.Layout_buttons.addWidget(self.But_edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Layout_buttons.addItem(self.horizontalSpacer)

        self.But_share = QComboBox(self.frame_for_buttons)
        icon2 = QIcon()
        icon2.addFile(u":/icons/for_app_ui_card/icons8-\u0432\u043d\u0435\u0448\u043d\u044f\u044f-\u0441\u0441\u044b\u043b\u043a\u0430-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_share.addItem(icon2, "")
        self.But_share.addItem("")
        self.But_share.addItem("")
        self.But_share.addItem("")
        self.But_share.setObjectName(u"But_share")
        self.But_share.setMinimumSize(QSize(80, 18))
        self.But_share.setMaximumSize(QSize(75, 18))
        self.But_share.setFont(font)
        self.But_share.setStyleSheet(u"QComboBox{\n"
"color: rgb(90, 90, 90);\n"
"width: 0px;\n"
"height: 0px;\n"
"border: 0px;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(210, 210, 210, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"width: 0px;\n"
"height: 0px;\n"
"border: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"selection-background-color: rgb(210, 210, 210);\n"
"selection-color:  rgb(90, 90, 90);\n"
"selection-border-color: rgb(200, 200, 200, 100);\n"
"color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"")
        self.But_share.setIconSize(QSize(16, 16))

        self.Layout_buttons.addWidget(self.But_share)

        self.But_del = QPushButton(self.frame_for_buttons)
        self.But_del.setObjectName(u"But_del")
        self.But_del.setMinimumSize(QSize(40, 18))
        self.But_del.setMaximumSize(QSize(20, 18))
        self.But_del.setFont(font)
        self.But_del.setStyleSheet(u"QPushButton {\n"
"color: rgb(90, 90, 90);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(210, 210, 210, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/for_app_ui_card/icons8-\u043c\u0443\u0441\u043e\u0440-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_del.setIcon(icon3)

        self.Layout_buttons.addWidget(self.But_del)


        self.horizontalLayout_2.addLayout(self.Layout_buttons)


        self.verticalLayout.addWidget(self.frame_for_buttons)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Frame_Picture = QFrame(Card_Window)
        self.Frame_Picture.setObjectName(u"Frame_Picture")
        self.Frame_Picture.setMinimumSize(QSize(261, 393))
        self.Frame_Picture.setMaximumSize(QSize(261, 393))
        self.Frame_Picture.setFrameShape(QFrame.StyledPanel)
        self.Frame_Picture.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Frame_Picture)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.label_Picture = QLabel(self.Frame_Picture)
        self.label_Picture.setObjectName(u"label_Picture")
        self.label_Picture.setMinimumSize(QSize(243, 375))
        self.label_Picture.setMaximumSize(QSize(243, 375))
        self.label_Picture.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_Picture)


        self.horizontalLayout.addWidget(self.Frame_Picture)

        self.Frame_TextBrowser = QFrame(Card_Window)
        self.Frame_TextBrowser.setObjectName(u"Frame_TextBrowser")
        self.Frame_TextBrowser.setFrameShape(QFrame.StyledPanel)
        self.Frame_TextBrowser.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Frame_TextBrowser)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.Label_category = QLabel(self.Frame_TextBrowser)
        self.Label_category.setObjectName(u"Label_category")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_category.sizePolicy().hasHeightForWidth())
        self.Label_category.setSizePolicy(sizePolicy)
        self.Label_category.setMinimumSize(QSize(55, 16))
        self.Label_category.setMaximumSize(QSize(50, 16))
        self.Label_category.setFont(font)
        self.Label_category.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.horizontalLayout_3.addWidget(self.Label_category)

        self.LineEdit_category = QLineEdit(self.Frame_TextBrowser)
        self.LineEdit_category.setObjectName(u"LineEdit_category")
        sizePolicy.setHeightForWidth(self.LineEdit_category.sizePolicy().hasHeightForWidth())
        self.LineEdit_category.setSizePolicy(sizePolicy)
        self.LineEdit_category.setMinimumSize(QSize(140, 16))
        self.LineEdit_category.setMaximumSize(QSize(100, 16))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        self.LineEdit_category.setFont(font1)
        self.LineEdit_category.setStyleSheet(u"border: 0px;\n"
"border-color: rgb(90, 90, 90);\n"
"color: rgb(90, 90, 90);\n"
"background-color: rgb(244, 244, 244);")
        self.LineEdit_category.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.LineEdit_category)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.Label_difficulty = QLabel(self.Frame_TextBrowser)
        self.Label_difficulty.setObjectName(u"Label_difficulty")
        sizePolicy.setHeightForWidth(self.Label_difficulty.sizePolicy().hasHeightForWidth())
        self.Label_difficulty.setSizePolicy(sizePolicy)
        self.Label_difficulty.setMinimumSize(QSize(55, 16))
        self.Label_difficulty.setMaximumSize(QSize(50, 16))
        self.Label_difficulty.setFont(font)
        self.Label_difficulty.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.horizontalLayout_5.addWidget(self.Label_difficulty)

        self.ComboBox_difficulty = QComboBox(self.Frame_TextBrowser)
        icon4 = QIcon()
        icon4.addFile(u":/icons/for_app_ui_card/star_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/for_app_ui_card/star_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/for_app_ui_card/star_3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/for_app_ui_card/star_4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/icons/for_app_ui_card/star_5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon8, "")
        self.ComboBox_difficulty.setObjectName(u"ComboBox_difficulty")
        self.ComboBox_difficulty.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ComboBox_difficulty.sizePolicy().hasHeightForWidth())
        self.ComboBox_difficulty.setSizePolicy(sizePolicy)
        self.ComboBox_difficulty.setMinimumSize(QSize(140, 16))
        self.ComboBox_difficulty.setMaximumSize(QSize(100, 16))
        self.ComboBox_difficulty.setFont(font)
        self.ComboBox_difficulty.setStyleSheet(u"QComboBox{\n"
"color: rgb(90, 90, 90);\n"
"width: 0px;\n"
"height: 0px;\n"
"border: 0px;\n"
"background-color: rgb(244, 244, 244);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"width: 0px;\n"
"height: 0px;\n"
"border: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"selection-background-color: rgb(244, 244, 244);\n"
"selection-color:  rgb(90, 90, 90);\n"
"color: rgb(90, 90, 90);\n"
"}")
        self.ComboBox_difficulty.setEditable(True)
        self.ComboBox_difficulty.setIconSize(QSize(150, 150))

        self.horizontalLayout_5.addWidget(self.ComboBox_difficulty)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.TextBrowser_task = QTextBrowser(self.Frame_TextBrowser)
        self.TextBrowser_task.setObjectName(u"TextBrowser_task")
        self.TextBrowser_task.setEnabled(True)
        self.TextBrowser_task.setMaximumSize(QSize(16777215, 365))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.TextBrowser_task.setFont(font2)
        self.TextBrowser_task.setStyleSheet(u"border: 0px;\n"
"border-color: rgb(90, 90, 90);\n"
"color: rgb(90, 90, 90);\n"
"background-color: rgb(244, 244, 244);\n"
"")
        self.TextBrowser_task.setLineWidth(1)
        self.TextBrowser_task.setAutoFormatting(QTextEdit.AutoNone)
        self.TextBrowser_task.setLineWrapColumnOrWidth(0)
        self.TextBrowser_task.setReadOnly(True)
        self.TextBrowser_task.setOverwriteMode(False)
        self.TextBrowser_task.setTabStopDistance(20.000000000000000)

        self.verticalLayout_3.addWidget(self.TextBrowser_task)


        self.horizontalLayout.addWidget(self.Frame_TextBrowser)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Card_Window)

        QMetaObject.connectSlotsByName(Card_Window)
    # setupUi

    def retranslateUi(self, Card_Window):
        Card_Window.setWindowTitle(QCoreApplication.translate("Card_Window", u"Dialog", None))
        self.But_flag.setText(QCoreApplication.translate("Card_Window", u"Ready", None))
        self.But_edit.setText(QCoreApplication.translate("Card_Window", u"Edit", None))
        self.But_share.setItemText(0, QCoreApplication.translate("Card_Window", u"Share", None))
        self.But_share.setItemText(1, QCoreApplication.translate("Card_Window", u"Card", None))
        self.But_share.setItemText(2, QCoreApplication.translate("Card_Window", u"Category", None))
        self.But_share.setItemText(3, QCoreApplication.translate("Card_Window", u"All", None))

        self.But_share.setCurrentText(QCoreApplication.translate("Card_Window", u"Share", None))
        self.But_del.setText(QCoreApplication.translate("Card_Window", u"Del", None))
        self.label_Picture.setText("")
        self.Label_category.setText(QCoreApplication.translate("Card_Window", u"\u0421ategory:", None))
        self.Label_difficulty.setText(QCoreApplication.translate("Card_Window", u"Difficulty:", None))
        self.ComboBox_difficulty.setItemText(0, QCoreApplication.translate("Card_Window", u"\u00a0", None))
        self.ComboBox_difficulty.setItemText(1, QCoreApplication.translate("Card_Window", u"\u00a0", None))
        self.ComboBox_difficulty.setItemText(2, QCoreApplication.translate("Card_Window", u"\u00a0", None))
        self.ComboBox_difficulty.setItemText(3, QCoreApplication.translate("Card_Window", u"\u00a0", None))
        self.ComboBox_difficulty.setItemText(4, QCoreApplication.translate("Card_Window", u"\u00a0", None))

        self.TextBrowser_task.setHtml(QCoreApplication.translate("Card_Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

