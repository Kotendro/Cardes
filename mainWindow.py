import shutil
from os import remove, path

from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication
from PySide6 import QtCore, QtGui
from PySide6.QtGui import QIcon
from PIL import Image

from mainUI import Ui_Main_Window

from card import CardWidget
from help import Help
from cardWindow import CardWindow

from flowLayout import FlowLayout


class MainWindow(QMainWindow, Ui_Main_Window):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Cardes')
        self.setWindowIcon(QIcon('ico_app.png'))
        # Special grid-like layout that automatically positions new items in rows according to available space
        self.Layout_flow = FlowLayout()

        # Load existing cards from the database, show the ones that match current filters
        # self.setup_card_data()

        # Load card categories from the cards themselves(!), fill up the Categories filter selection box
        # self.setup_categories()

        self.Layout_scrollArea.addLayout(self.Layout_flow)

        self.But_add.clicked.connect(self.add_button)
        # self.But_open.clicked.connect(self.open_card)
        self.But_help.clicked.connect(self.create_help_window)

        self.ComboBox_sorting.currentTextChanged.connect(self.change_sorting)
        self.ComboBox_categories.currentTextChanged.connect(self.change_sorting)
        self.ComboBox_difficulty.currentIndexChanged.connect(self.change_sorting)

    # def setup_card_data(self):
    #     def create_widget_in_area():
    #         card = CardWidget(id_card, value[0], value[1], value[2], value[3])
    #         self.Layout_flow.addWidget(card)
    #         self.settings_icon_card(card, value[0], id_card)
    #         card.create_card_window.connect(self.create_card_window)
    #
    #     def sorting_categories():
    #         if self.ComboBox_categories.currentText() == 'all':
    #             return True
    #         elif self.ComboBox_categories.currentText() == value[2]:
    #             return True
    #         else:
    #             return False
    #
    #     def sorting_diff():
    #         if self.ComboBox_difficulty.currentIndex() == 0:
    #             create_widget_in_area()
    #         elif self.ComboBox_difficulty.currentIndex() - 1 == value[3]:
    #             create_widget_in_area()
    #         else:
    #             pass
    #
    #     with shelve.open('Data\Card') as dat:
    #         if self.ComboBox_sorting.currentText() == 'all':
    #             for id_card, value in dat.items():
    #                 if sorting_categories():
    #                     sorting_diff()
    #
    #         if self.ComboBox_sorting.currentText() == 'completed':
    #             for id_card, value in dat.items():
    #                 if value[0] == 1:
    #                     if sorting_categories():
    #                         sorting_diff()
    #                 if value[0] == 0:
    #                     pass
    #
    #         if self.ComboBox_sorting.currentText() == 'uncompleted':
    #             for id_card, value in dat.items():
    #                 if value[0] == 0:
    #                     if sorting_categories():
    #                         sorting_diff()
    #                 if value[0] == 1:
    #                     pass

    # def setup_categories(self):
    #     current = self.ComboBox_categories.currentText()
    #     allItems = []
    #
    #     self.ComboBox_categories.clear()
    #     self.ComboBox_categories.addItem('all')
    #
    #     with shelve.open('Data\Card') as dat:
    #         for value in dat.values():
    #             allItems = [self.ComboBox_categories.itemText(i) for i in range(self.ComboBox_categories.count())]
    #
    #             if value[2] != None and value[2] != '' and value[2] not in allItems:
    #                 self.ComboBox_categories.addItem(value[2])
    #     if current in allItems:
    #         self.ComboBox_categories.setCurrentText(current)
    #     else:
    #         pass

    # def save_data(self, widget, flag, task, category, diff):
    #     with shelve.open('Data\Card') as dat:
    #         dat[f'{widget.id_card}'] = [flag, task, category, diff]

    # def del_data(self, id_card):
    #     remove(f'Pictures\{id_card}.png')
    #     remove(f'BlackAndWhite_Pictures\{id_card}.png')
    #
    #     with shelve.open('Data\Card') as dat:
    #         del dat[f'{id_card}']
    #
    #     with shelve.open('Data\Card_id') as dat:
    #         for value in dat.values():
    #             value.remove(int(id_card))
    #             dat['id_card'] = sorted(value)
    #
    # def settings_icon_card(self, card_widget, flag, id_card):
    #     if flag == 0:
    #         card_widget.But_Card_widget.setIcon(QtGui.QIcon(f'BlackAndWhite_Pictures\{id_card}.png'))
    #     else:
    #         card_widget.But_Card_widget.setIcon(QtGui.QIcon(f'Pictures\{id_card}.png'))
    #     card_widget.But_Card_widget.setIconSize(QtCore.QSize(162, 250))

    # def add_button(self):
    #
    #     picture = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'PNG Image (*.png);; JPEG Image (*.jpg);')
    #
    #     if picture[0] != '':
    #         self.setup_id_card()
    #
    #         with Image.open(picture[0]) as image_copy:  # копирование файла
    #             image_copy.save(f'Pictures\{self.id_card}.png')
    #             blackAndWhite = image_copy.convert('L')
    #             blackAndWhite.save(f'BlackAndWhite_Pictures\{self.id_card}.png')
    #
    #         card = CardWidget(self.id_card, 0, None, 'all', 0)
    #
    #         self.save_data(card, 0, None, 'all', 0)
    #         self.change_sorting()
    #
    #         card.create_card_window.connect(self.create_card_window)

    # def open_card(self):
    #     open_dir = QFileDialog.getExistingDirectory(self, 'Открыть', None)
    #
    #     if path.exists(f'{open_dir}\CardShare.dat') == True:
    #         with shelve.open(f'{open_dir}\CardShare') as dat:
    #             for id_card, value in dat.items():
    #                 self.setup_id_card()
    #
    #                 with Image.open(f'{open_dir}\{id_card}.png') as image_copy:
    #                     image_copy.save(f'Pictures\{self.id_card}.png')
    #                     blackAndWhite = image_copy.convert('L')
    #                     blackAndWhite.save(f'BlackAndWhite_Pictures\{self.id_card}.png')
    #
    #                 card = CardWidget(self.id_card, value[0], value[1], value[2], value[3])
    #                 self.save_data(card, value[0], value[1], value[2], value[3])
    #
    #         shutil.rmtree(open_dir)
    #
    #         self.change_sorting()
    #
    #         card.create_card_window.connect(self.create_card_window)

    def create_help_window(self):
        self.help = Help()
        self.help.show()

    def create_card_window(self):
        widget = self.sender()
        self.card_window = CardWindow(widget, widget.flag, widget.edit, widget.category, widget.diff, self.pos().x(),
                                      self.pos().y())
        self.card_window.show()
        self.ComboBox_sorting.setEnabled(0)
        self.ComboBox_categories.setEnabled(0)
        self.ComboBox_difficulty.setEnabled(0)

        self.card_window.delete.connect(self.del_button)
        self.card_window.flag_signal.connect(self.change_flag)
        self.card_window.edit_signal.connect(self.change_edit)
        self.card_window.close_signal.connect(self.close_card_window_sorting)

    def del_button(self, widget):
        print(f"{widget.id_card} удалено")
        self.Layout_flow.removeWidget(widget)
        widget.deleteLater()
        # self.del_data(widget.id_card)
        # self.setup_categories()

    def clear_area(self):
        while self.Layout_flow.count() > 0:
            item = self.Layout_flow.takeAt(0)
            item.widget().deleteLater()

    def change_flag(self, widget):
        widget_window = self.sender()
        # self.settings_icon_card(widget, widget.flag, widget.id_card)
        # self.save_data(widget, widget.flag, widget_window.task, widget_window.category, widget_window.diff)

    def change_edit(self, widget):
        widget_window = self.sender()
        # self.save_data(widget, widget.flag, widget_window.task, widget_window.category, widget_window.diff)

    def change_sorting(self):
        self.clear_area()
        # self.setup_card_data()

    def close_card_window_sorting(self):
        self.change_sorting()
        # self.setup_categories()
        self.ComboBox_sorting.setEnabled(1)
        self.ComboBox_categories.setEnabled(1)
        self.ComboBox_difficulty.setEnabled(1)

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        return super(MainWindow, self).closeEvent(event)
