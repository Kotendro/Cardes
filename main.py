import sys

from PySide6.QtWidgets import QApplication

from mainWindow import MainWindow


def check_connectivity():
    pass


def update():
    pass


def setup_cache():
    pass


if __name__ == '__main__':
    check_connectivity()
    update()
    setup_cache()
    
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
