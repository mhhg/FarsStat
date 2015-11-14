from PyQt5.QtWidgets import QMenu, QMenuBar
from gui import FileMenu

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)

        self.file_menu = FileMenu(self)
        self.edit_menu = QMenu(self)
        self.view_menu = QMenu(self)
        self.window_menu = QMenu(self)
        self.help_menu = QMenu(self)

        self.addAction(self.file_menu.menuAction())
        self.addAction(self.edit_menu.menuAction())
        self.addAction(self.view_menu.menuAction())
        self.addAction(self.window_menu.menuAction())
        self.addAction(self.help_menu.menuAction())

        self.file_menu.setTitle("File")
        self.edit_menu.setTitle("Edit")
        self.view_menu.setTitle("View")
        self.window_menu.setTitle("Window")
        self.help_menu.setTitle("Help")
