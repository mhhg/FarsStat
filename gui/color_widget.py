from PyQt5.QtWidgets import QWidget, QColorDialog
from PyQt5.QtGui import QPalette, QColor


class ColorWidget(QWidget):
    def __init__(self, parent, default_color):
        super(ColorWidget, self).__init__(parent)
        if isinstance(default_color, str):
            default_color = QColor(default_color)
        self.color = default_color
        self.dlg = QColorDialog()
        self.palette = QPalette()

        self.properties()
        self.set_background()
        # self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

    def properties(self):
        self.setMinimumWidth(10)
        self.setMinimumHeight(20)
        self.dlg.setWindowTitle("Select Query Color")
        self.setAutoFillBackground(True)

    def mouseDoubleClickEvent(self, QMouseEvent):
        if self.dlg.exec() == QColorDialog.Accepted:
            self.color = self.dlg.selectedColor()
            self.set_background()

    def set_background(self):
        self.palette.setColor(QPalette.Background, self.color)
        self.setPalette(self.palette)
