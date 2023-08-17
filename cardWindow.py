import shelve
from os import mkdir
from PIL import Image

from PySide6 import QtGui
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QIcon

from cardWindowUI import Ui_Card_Window


class CardWindow(QWidget, Ui_Card_Window):
    delete = Signal(object)
    flag_signal = Signal(object)
    edit_signal = Signal(object)
    close_signal = Signal()

    def __init__(self, widget, flag, task, category, diff, x, y):
        super(CardWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Cardes')
        self.setWindowIcon(QIcon('ico_app.png'))

        self.move(x+1020, y)

        self.widget = widget
        self.flag = flag
        self.task = task
        self.category = category
        self.diff = diff
        self.edit_flag = 0

        self.x = x
        self.y = y

        self.setup_pos()
        self.setup_picture()
        self.setup_category()
        self.setup_diff()
        self.setup_edit()

        self.But_del.clicked.connect(self.press_del)
        self.But_flag.clicked.connect(self.press_flag)
        self.But_edit.clicked.connect(self.press_edit)
        self.But_share.currentIndexChanged.connect(self.press_share)

    def setup_pos(self):
        if self.x <= 800:
            self.move(self.x + 1020, self.y)
        else:
            self.move(self.x - 470, self.y)

    def setup_picture(self):
        if self.flag == 0:
            self.label_Picture.setPixmap(QtGui.QPixmap(f'BlackAndWhite_Pictures\{self.widget.id_card}.png'))
        else:
            self.label_Picture.setPixmap(QtGui.QPixmap(f'Pictures\{self.widget.id_card}.png'))

    def setup_diff(self):
        self.ComboBox_difficulty.setCurrentIndex(self.diff)

    def setup_category(self):
        if self.category == None or self.category == '':
            self.LineEdit_category.setText('all')
        else:
            self.LineEdit_category.setText(self.category)

    def setup_edit(self):
        self.TextBrowser_task.setText(self.task)

    def press_flag(self):

        if self.flag == 0:
            self.flag = 1
            self.widget.flag = 1
        elif self.flag == 1:
            self.flag = 0
            self.widget.flag = 0

        self.setup_picture()
        self.flag_signal.emit(self.widget)

    def press_edit(self):
        if self.edit_flag == 0:
            self.edit_flag = 1

            self.But_edit.setText('OK')
            self.Frame_TextBrowser.setStyleSheet(u"background-color: rgb(235, 235, 235);")

            self.But_flag.setEnabled(0)
            self.But_del.setEnabled(0)
            self.But_share.setEnabled(0)

            self.TextBrowser_task.setReadOnly(0)
            self.LineEdit_category.setReadOnly(0)
            self.ComboBox_difficulty.setEditable(0)

        elif self.edit_flag == 1:
            self.edit_flag = 0


            if self.LineEdit_category.text() == '':
                self.LineEdit_category.setText('all')
            self.But_edit.setText('Edit')
            self.Frame_TextBrowser.setStyleSheet(u"background-color: rgb(253, 253, 253);")

            self.But_flag.setEnabled(1)
            self.But_del.setEnabled(1)
            self.But_share.setEnabled(1)

            self.TextBrowser_task.setReadOnly(1)
            self.LineEdit_category.setReadOnly(1)
            self.ComboBox_difficulty.setEditable(1)

            self.task = self.TextBrowser_task.toPlainText()
            self.category = self.LineEdit_category.text()
            self.diff = self.ComboBox_difficulty.currentIndex()

            self.edit_signal.emit(self.widget)

    def press_del(self):
        self.delete.emit(self.widget)
        self.close()

    def press_share(self):
        share_type = self.But_share.currentIndex()
        self.But_share.setCurrentIndex(0)

        if share_type == 0:
            pass

        elif share_type == 1: # Карта
            try:
                path_save = QFileDialog.getExistingDirectory(self, 'Сохранить', None)
                if path_save != '':

                    mkdir(f'{path_save}/Shared_{self.widget.id_card}')

                    with shelve.open(f'{path_save}\Shared_{self.widget.id_card}\CardShare') as dat:
                        dat[f'{self.widget.id_card}'] = [0, self.task, self.category, self.diff]

                    with Image.open(f'Pictures\{self.widget.id_card}.png') as image_copy:  # копирование файла
                        image_copy.save(f'{path_save}\Shared_{self.widget.id_card}\{self.widget.id_card}.png')
            except FileExistsError:
                pass

        elif share_type == 2: # Категория
            try:
                path_save = QFileDialog.getExistingDirectory(self, 'Сохранить', None)
                if path_save != '':

                    mkdir(f'{path_save}/Shared_{self.category}_category')

                    with shelve.open(f'{path_save}\Shared_{self.category}_category\CardShare') as dat:
                        with shelve.open('Data\Card') as dat_prog:
                            for id_card, value in dat_prog.items():
                                if value[2] == self.category:
                                    dat[f'{id_card}'] = [0, value[1], value[2], value[3]]

                                    with Image.open(f'Pictures\{id_card}.png') as image_copy:  # копирование файла
                                        image_copy.save(f'{path_save}\Shared_{self.category}_category\{id_card}.png')
            except FileExistsError:
                pass

        elif share_type == 3:  # Всё
            try:
                path_save = QFileDialog.getExistingDirectory(self, 'Сохранить', None)
                if path_save != '':

                    mkdir(f'{path_save}/Shared_all')

                    with shelve.open(f'{path_save}\Shared_all\CardShare') as dat:
                        with shelve.open('Data\Card') as dat_prog:
                            for id_card, value in dat_prog.items():
                                dat[f'{id_card}'] = [0, value[1], value[2], value[3]]

                                with Image.open(f'Pictures/{id_card}.png') as image_copy:  # копирование файла
                                    image_copy.save(f'{path_save}\Shared_all\{id_card}.png')
            except FileExistsError:
                pass

    def closeEvent(self, event):
        self.close_signal.emit()
        return super(CardWindow, self).closeEvent(event)
