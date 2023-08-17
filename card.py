from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from cardUI import Ui_Card_widget


class CardWidget(QWidget, Ui_Card_widget):
    create_card_window = Signal()

    def __init__(self, id_card, flag, edit, category, diff):
        super(CardWidget, self).__init__()
        self.setupUi(self)
        self.id_card = id_card
        self.flag = flag
        self.edit = edit
        self.diff = diff
        self.category = category

        self.But_Card_widget.clicked.connect(self.press_card)

    def press_card(self):
        self.create_card_window.emit()
