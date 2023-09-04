from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton, QHBoxLayout
import PySide6.QtGui
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QColor,
                           QPen,
                           QStaticText,
                           QFont,
                           QRadialGradient,
                           QScreen,
                           QPalette,
                           QConicalGradient,
                           QPixmap
                           )
from PySide6.QtCore import QSize, Qt, QPoint, QMargins, QRect, QLine, QThreadPool


class CloseButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(QSize(25, 25))

    def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(painter.RenderHint.Antialiasing)

        brush = QBrush(QColor(200, 10, 10))
        brush.setStyle(Qt.BrushStyle.SolidPattern)

        painter.setBrush(brush)
        painter.drawEllipse(self.rect())

        painter.setPen(QPen(QColor(200, 200, 200), 3))
        painter.drawLines(
            [QLine(QPoint(self.width() // 4, self.height() // 4),
                   QPoint(self.width() * 3 // 4, self.height() * 3 // 4)),
             QLine(QPoint(self.width() // 4, self.height() * 3 // 4),
                   QPoint(self.width() * 3 // 4, self.height() // 4))])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(QSize(250, 270))

        self.update_btn = Updater(self)
        self.close_btn = CloseButton(self)

        self.close_btn.move(220, 5)
        self.update_btn.move(25, 35)

        self.close_btn.clicked.connect(self.close)

        self.drag_rect = QRect(0, 0, 250, 30)
        self.dragging = None

        self.threadpool = QThreadPool()

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.drag_rect.contains(event.position().toPoint()):
            self.dragging = event.position().toPoint()

    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if self.dragging and event.button() == Qt.MouseButton.LeftButton:
            self.dragging = None

    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.dragging)

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(painter.RenderHint.Antialiasing)

        painter.setBrush(self.palette().brush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window))
        painter.drawRoundedRect(self.rect(), 15, 15)

        br = QBrush(Qt.BrushStyle.Dense3Pattern)
        br.setColor(QColor(30, 60, 150, 80))

        painter.setBrush(br)
        painter.drawRoundedRect(self.rect(), 15, 15)

        # TODO: Remove this stupid gradient and draw circles normally
        grad = QRadialGradient(self.rect().center(), 20)
        grad.setSpread(grad.Spread.RepeatSpread)
        grad.setColorAt(0, QColor(50, 50, 50))
        grad.setColorAt(1, QColor(110, 110, 110))

        painter.setPen(QPen(grad, 20))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(self.update_btn.geometry().marginsRemoved(QMargins(20, 20, 20, 20)))


class Updater(QWidget):
    debugPen = QPen(QColor(255, 0, 0))
    lightBlueGradient = QRadialGradient(QRect(0, 0, 200, 200).center(), 60)
    lightBlueGradient.setSpread(QRadialGradient.Spread.RepeatSpread)
    lightBlueGradient.setColorAt(0, QColor(80, 180, 220))
    lightBlueGradient.setColorAt(0.5, QColor(130, 220, 255))
    lightBlueGradient.setColorAt(1, QColor(140, 220, 220))

    lightGreenGradient = QRadialGradient(QRect(0, 0, 200, 200).center(), 60)
    lightGreenGradient.setSpread(QRadialGradient.Spread.RepeatSpread)
    lightGreenGradient.setColorAt(0, QColor(80, 200, 100))
    lightGreenGradient.setColorAt(0.5, QColor(80, 172, 100))
    lightGreenGradient.setColorAt(1, QColor(150, 220, 150))

    def __init__(self, parent):
        super().__init__(parent)
        self.text = QStaticText("Update")
        self.setFixedSize(QSize(200, 200))

        self.circleBoundingRect = QRect(0, 0, 140, 140)
        self.circleBoundingRect.moveCenter(self.rect().center() - QPoint(1, 1))

    def debugPaint(self):
        painter = QPainter(self)

        painter.setPen(self.debugPen)
        painter.drawRect(self.rect().marginsRemoved(QMargins(0, 0, 1, 1)))
        painter.drawRect(self.circleBoundingRect)

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        # circle = QBrush(self.lightGreenGradient)
        circle = QBrush(self.lightBlueGradient)
        circle.setStyle(Qt.BrushStyle.RadialGradientPattern)
        black = QPen(QColor(0, 0, 0))
        gray = QPen(QColor(100, 100, 100))
        gray.setWidth(5)

        painter = QPainter(self)
        painter.setFont(QFont("Arial", 25, 700))
        painter.setRenderHints(QPainter.Antialiasing | QPainter.RenderHint.TextAntialiasing)

        painter.setBrush(circle)
        painter.drawEllipse(self.circleBoundingRect)

        painter.setPen(black)
        self.text.prepare(font=painter.font())
        painter.drawStaticText((self.width() - self.text.size().width()) / 2,
                               (self.height() - self.text.size().height()) / 2,
                               self.text)

        painter.setPen(gray)
        r = self.circleBoundingRect.marginsRemoved(QMargins(5, 5, 5, 5))
        painter.drawArc(r, -15 * 16, 90 * 16)
        painter.drawArc(r, 190 * 16, 70 * 16)

        painter.setPen(QPen(QColor(30, 30, 30), 5))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(r.marginsAdded(QMargins(7, 7, 7, 7)))


def setup_palette(application: QApplication):
    p = application.palette()

    gradient = QConicalGradient(125, 150, -90)
    gradient.setSpread(gradient.Spread.RepeatSpread)
    gradient.setColorAt(1, QColor(40, 40, 40))
    gradient.setColorAt(0.5, QColor(90, 90, 90))
    gradient.setColorAt(0, QColor(40, 40, 40))
    br = QBrush(gradient)
    br.setStyle(Qt.BrushStyle.ConicalGradientPattern)

    p.setBrush(p.ColorGroup.All, p.ColorRole.Window, br)
    return p


if __name__ == '__main__':
    app = QApplication()
    palette = setup_palette(app)
    window = Window()
    window.setPalette(palette)
    window.show()
    app.exec()
