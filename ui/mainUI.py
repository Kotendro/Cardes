# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resMain_rc

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName(u"Main_Window")
        Main_Window.resize(1020, 621)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main_Window.sizePolicy().hasHeightForWidth())
        Main_Window.setSizePolicy(sizePolicy)
        Main_Window.setMinimumSize(QSize(1020, 621))
        Main_Window.setMaximumSize(QSize(1020, 621))
        Main_Window.setStyleSheet(u"background-color: rgb(253, 253, 253);")
        self.centralwidget = QWidget(Main_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 36))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Label_sorting = QLabel(self.frame)
        self.Label_sorting.setObjectName(u"Label_sorting")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Label_sorting.sizePolicy().hasHeightForWidth())
        self.Label_sorting.setSizePolicy(sizePolicy2)
        self.Label_sorting.setMinimumSize(QSize(0, 18))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.Label_sorting.setFont(font1)
        self.Label_sorting.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.horizontalLayout.addWidget(self.Label_sorting)

        self.ComboBox_sorting = QComboBox(self.frame)
        self.ComboBox_sorting.addItem("")
        self.ComboBox_sorting.addItem("")
        self.ComboBox_sorting.addItem("")
        self.ComboBox_sorting.setObjectName(u"ComboBox_sorting")
        self.ComboBox_sorting.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ComboBox_sorting.sizePolicy().hasHeightForWidth())
        self.ComboBox_sorting.setSizePolicy(sizePolicy)
        self.ComboBox_sorting.setMinimumSize(QSize(100, 18))
        self.ComboBox_sorting.setMaximumSize(QSize(16777215, 18))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.ComboBox_sorting.setFont(font2)
        self.ComboBox_sorting.setCursor(QCursor(Qt.ArrowCursor))
        self.ComboBox_sorting.setMouseTracking(False)
        self.ComboBox_sorting.setTabletTracking(False)
        self.ComboBox_sorting.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ComboBox_sorting.setStyleSheet(u"QComboBox{\n"
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
"\n"
"\n"
"\n"
"")
        self.ComboBox_sorting.setEditable(False)
        self.ComboBox_sorting.setInsertPolicy(QComboBox.InsertAtBottom)
        self.ComboBox_sorting.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.ComboBox_sorting.setDuplicatesEnabled(False)
        self.ComboBox_sorting.setFrame(True)
        self.ComboBox_sorting.setModelColumn(0)

        self.horizontalLayout.addWidget(self.ComboBox_sorting)

        self.Label_categories = QLabel(self.frame)
        self.Label_categories.setObjectName(u"Label_categories")
        self.Label_categories.setMinimumSize(QSize(0, 18))
        self.Label_categories.setMaximumSize(QSize(16777215, 18))
        self.Label_categories.setFont(font1)
        self.Label_categories.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.horizontalLayout.addWidget(self.Label_categories)

        self.ComboBox_categories = QComboBox(self.frame)
        self.ComboBox_categories.addItem("")
        self.ComboBox_categories.setObjectName(u"ComboBox_categories")
        self.ComboBox_categories.setMinimumSize(QSize(100, 18))
        self.ComboBox_categories.setMaximumSize(QSize(16777215, 18))
        self.ComboBox_categories.setFont(font1)
        self.ComboBox_categories.setStyleSheet(u"QComboBox{\n"
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
"}")
        self.ComboBox_categories.setDuplicatesEnabled(True)

        self.horizontalLayout.addWidget(self.ComboBox_categories)

        self.Label_difficulty = QLabel(self.frame)
        self.Label_difficulty.setObjectName(u"Label_difficulty")
        self.Label_difficulty.setMinimumSize(QSize(0, 18))
        self.Label_difficulty.setMaximumSize(QSize(16777215, 18))
        self.Label_difficulty.setFont(font1)
        self.Label_difficulty.setStyleSheet(u"color: rgb(90, 90, 90);")

        self.horizontalLayout.addWidget(self.Label_difficulty)

        self.ComboBox_difficulty = QComboBox(self.frame)
        self.ComboBox_difficulty.addItem("")
        icon = QIcon()
        icon.addFile(u":/icons/for_app_ui/star_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/for_app_ui/star_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/for_app_ui/star_3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/for_app_ui/star_4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/for_app_ui/star_5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ComboBox_difficulty.addItem(icon4, "")
        self.ComboBox_difficulty.setObjectName(u"ComboBox_difficulty")
        self.ComboBox_difficulty.setMinimumSize(QSize(100, 18))
        self.ComboBox_difficulty.setMaximumSize(QSize(16777215, 18))
        self.ComboBox_difficulty.setFont(font1)
        self.ComboBox_difficulty.setStyleSheet(u"QComboBox{\n"
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
"}")
        self.ComboBox_difficulty.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.ComboBox_difficulty)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.But_help = QPushButton(self.frame)
        self.But_help.setObjectName(u"But_help")
        self.But_help.setMinimumSize(QSize(50, 18))
        self.But_help.setMaximumSize(QSize(50, 18))
        self.But_help.setFont(font2)
        self.But_help.setStyleSheet(u"QPushButton {\n"
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
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/for_app_ui/icons8-\u043f\u043e\u0438\u0441\u043a-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_help.setIcon(icon5)

        self.horizontalLayout.addWidget(self.But_help)

        self.But_open = QPushButton(self.frame)
        self.But_open.setObjectName(u"But_open")
        self.But_open.setMinimumSize(QSize(75, 18))
        self.But_open.setMaximumSize(QSize(16777215, 18))
        self.But_open.setFont(font1)
        self.But_open.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/for_app_ui/icons8-\u0444\u0430\u0439\u043b-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_open.setIcon(icon6)

        self.horizontalLayout.addWidget(self.But_open)

        self.But_add = QPushButton(self.frame)
        self.But_add.setObjectName(u"But_add")
        self.But_add.setMinimumSize(QSize(75, 18))
        self.But_add.setMaximumSize(QSize(75, 18))
        self.But_add.setFont(font1)
        self.But_add.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/for_app_ui/icons8-\u043f\u043b\u044e\u0441-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.But_add.setIcon(icon7)

        self.horizontalLayout.addWidget(self.But_add)


        self.verticalLayout.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"border: 0px\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"	background-color: rgb(217, 217, 217)\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	\n"
"	color: rgb(255, 26, 76);\n"
"    background:	rgb(210, 210, 210);\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1020, 585))
        self.scrollAreaWidgetContents.setStyleSheet(u"\n"
"border: 0px;\n"
"background-color: qradialgradient(spread:reflect, cx:0.506, cy:0, radius:1.104, fx:0.505682, fy:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(224, 224, 224, 255));")
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Layout_scrollArea = QVBoxLayout()
        self.Layout_scrollArea.setSpacing(0)
        self.Layout_scrollArea.setObjectName(u"Layout_scrollArea")

        self.horizontalLayout_2.addLayout(self.Layout_scrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Window)

        self.ComboBox_sorting.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main_Window)
    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(QCoreApplication.translate("Main_Window", u"MainWindow", None))
        self.Label_sorting.setText(QCoreApplication.translate("Main_Window", u"Sorting:", None))
        self.ComboBox_sorting.setItemText(0, QCoreApplication.translate("Main_Window", u"all", None))
        self.ComboBox_sorting.setItemText(1, QCoreApplication.translate("Main_Window", u"completed", None))
        self.ComboBox_sorting.setItemText(2, QCoreApplication.translate("Main_Window", u"uncompleted", None))

        self.Label_categories.setText(QCoreApplication.translate("Main_Window", u"\u0421ategories:", None))
        self.ComboBox_categories.setItemText(0, QCoreApplication.translate("Main_Window", u"all", None))

        self.Label_difficulty.setText(QCoreApplication.translate("Main_Window", u"Difficulty:", None))
        self.ComboBox_difficulty.setItemText(0, QCoreApplication.translate("Main_Window", u"all", None))
        self.ComboBox_difficulty.setItemText(1, "")
        self.ComboBox_difficulty.setItemText(2, "")
        self.ComboBox_difficulty.setItemText(3, "")
        self.ComboBox_difficulty.setItemText(4, "")
        self.ComboBox_difficulty.setItemText(5, "")

        self.But_help.setText(QCoreApplication.translate("Main_Window", u"Help", None))
        self.But_open.setText(QCoreApplication.translate("Main_Window", u"Open", None))
        self.But_add.setText(QCoreApplication.translate("Main_Window", u"Add", None))
    # retranslateUi

