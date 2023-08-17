from PySide6 import QtGui
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from helpUI import Ui_Help_Window

class Help(QWidget, Ui_Help_Window):

    def __init__(self):
        super(Help, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Cardes')
        self.setWindowIcon(QIcon('ico_app.png'))