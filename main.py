import shelve
import sys
from os import mkdir, path

from PySide6.QtWidgets import QApplication

from mainWindow import MainWindow


def create_pictures_dir():
    try:
        mkdir('Pictures')
    except FileExistsError:
        pass


def create_BAW_pictures_dir():
    try:
        mkdir('BlackAndWhite_Pictures')
    except FileExistsError:
        pass


def create_data_dir():
    try:
        mkdir('Data')
    except FileExistsError:
        pass


def create_shelve_data():
    if not path.exists('Data\Card.dat'):
        shelve.open('Data\Card')


def create_shelve_card_id():
    if not path.exists('Data\Card_id.dat'):
        shelve.open('Data\Card_id')
        with shelve.open('Data\Card_id') as dat:
            dat['id_card'] = [0]


if __name__ == '__main__':
    create_pictures_dir()
    create_BAW_pictures_dir()
    create_data_dir()

    create_shelve_data()
    create_shelve_card_id()

    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
