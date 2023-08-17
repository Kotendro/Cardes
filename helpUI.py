# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QSizePolicy,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Help_Window(object):
    def setupUi(self, Help_Window):
        if not Help_Window.objectName():
            Help_Window.setObjectName(u"Help_Window")
        Help_Window.resize(360, 225)
        Help_Window.setMinimumSize(QSize(360, 225))
        Help_Window.setMaximumSize(QSize(360, 225))
        Help_Window.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.verticalLayout = QVBoxLayout(Help_Window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TabWidget = QTabWidget(Help_Window)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setMinimumSize(QSize(0, 0))
        self.TabWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        font.setBold(True)
        self.TabWidget.setFont(font)
        self.TabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"         border-top: 4px solid #d9d9d9;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"alignment: center;\n"
"\n"
"}\n"
"\n"
"QTabBar{\n"
"	color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"color: rgb(90, 90, 90);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(210, 210, 210, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.914773, x2:1, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.0454545 rgba(184, 184, 184, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.TabWidget.setTabShape(QTabWidget.Rounded)
        self.TabWidget.setElideMode(Qt.ElideNone)
        self.TabWidget.setDocumentMode(False)
        self.TabWidget.setTabsClosable(False)
        self.TabWidget.setMovable(False)
        self.TabWidget.setTabBarAutoHide(False)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.506, cy:0, radius:1.104, fx:0.505682, fy:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(224, 224, 224, 255));")
        self.horizontalLayout = QHBoxLayout(self.page1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.page1)
        self.textBrowser.setObjectName(u"textBrowser")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        self.textBrowser.setFont(font1)
        self.textBrowser.setStyleSheet(u"border: none;\n"
"color: rgb(70, 70, 70);")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.TabWidget.addTab(self.page1, "")
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.506, cy:0, radius:1.104, fx:0.505682, fy:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(224, 224, 224, 255));")
        self.horizontalLayout_2 = QHBoxLayout(self.page2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_2 = QTextBrowser(self.page2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setFont(font1)
        self.textBrowser_2.setStyleSheet(u"border: none;\n"
"color: rgb(70, 70, 70);")

        self.horizontalLayout_2.addWidget(self.textBrowser_2)

        self.TabWidget.addTab(self.page2, "")
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.page3.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.506, cy:0, radius:1.104, fx:0.505682, fy:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(224, 224, 224, 255));")
        self.horizontalLayout_3 = QHBoxLayout(self.page3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_3 = QTextBrowser(self.page3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setFont(font1)
        self.textBrowser_3.setStyleSheet(u"border: none;\n"
"color: rgb(70, 70, 70);")

        self.horizontalLayout_3.addWidget(self.textBrowser_3)

        self.TabWidget.addTab(self.page3, "")
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.page4.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.506, cy:0, radius:1.104, fx:0.505682, fy:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(224, 224, 224, 255));")
        self.horizontalLayout_4 = QHBoxLayout(self.page4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_4 = QTextBrowser(self.page4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setFont(font1)
        self.textBrowser_4.setStyleSheet(u"border: none;\n"
"color: rgb(70, 70, 70);")

        self.horizontalLayout_4.addWidget(self.textBrowser_4)

        self.TabWidget.addTab(self.page4, "")

        self.verticalLayout.addWidget(self.TabWidget)


        self.retranslateUi(Help_Window)

        self.TabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Help_Window)
    # setupUi

    def retranslateUi(self, Help_Window):
        Help_Window.setWindowTitle(QCoreApplication.translate("Help_Window", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Help_Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In the program it is possible to sort cards by:<br />&gt; <span style=\" font-weight:600;\">Sorting </span>- all cards, completed cards, uncompleted cards;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Categories </span>- sort by categories added by you;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span"
                        " style=\" font-weight:600;\">&gt; Difficulty </span>- sort by difficulty that you assign.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button<span style=\" font-weight:600;\"> Open </span>can open shared cards (select a folder).</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button<span style=\" font-weight:600;\"> Add </span>append your cards (select an image).</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\">When you add your card, you can click on it by opening its editing (read more in the card window).</p></body></html>", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.page1), QCoreApplication.translate("Help_Window", u"Main window", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Help_Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button <span style=\" font-weight:600;\">Ready</span> changes the color of the card, which indicates completion/uncompletion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button <span style=\" font-weight:600;\">Edit</span> enable change:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Category</span>;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Difficulty</span>;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Text to the card</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button <span style=\" font-weight:600;\">Share </span>allows you to share the cards (create a folder).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button <span style="
                        "\" font-weight:600;\">Del</span> deletes the card.</p></body></html>", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.page2), QCoreApplication.translate("Help_Window", u"Card window", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Help_Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For correct display, the card must have a resolution of <span style=\" font-weight:600;\">324 x 500</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The card should preferably have:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span"
                        " style=\" font-weight:600;\">&gt; Name</span>;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Name of the game</span>;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Picture showing the essence of the task</span>;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&gt; Difficulty</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After adding the card, add the task to it, change the difficulty and add the category via th"
                        "e <span style=\" font-weight:600;\">Edit</span> button (read more in the Card window).</p></body></html>", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.page3), QCoreApplication.translate("Help_Window", u"Card format", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Help_Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The program was created by <span style=\" font-weight:600;\">Kotendro</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the concept was invented by <span style=\" font-weight:600;\">Kotendro</span>, <span style=\" font-weight:600;\">Teapare</span>, <span style=\" font-weight:600;\">BlackPanther</spa"
                        "n>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">icons by Icons8.</p></body></html>", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.page4), QCoreApplication.translate("Help_Window", u"Info", None))
    # retranslateUi

