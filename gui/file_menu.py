import logging
from models import Writer
from PyQt5.QtWidgets import QMenu, QAction, QFileDialog, QMessageBox
import os
logger = logging.getLogger("FS")


class FileMenu(QMenu):
    def __init__(self, parent):
        super(FileMenu, self).__init__(parent)

        self.open_action = QAction('&Open', self)
        self.save_action = QAction('&Save', self)
        self.save_as_action = QAction('Save &As', self)
        self.exit = QAction('&Exit', self)

        self.add_actions()
        self.events()

    def add_actions(self):
        self.addAction(self.open_action)
        self.addAction(self.save_action)
        self.addAction(self.save_as_action)
        self.addAction(self.exit)

    def events(self):
        self.open_action.triggered.connect(self.open)
        self.save_as_action.triggered.connect(self.save_as)

    def open(self, event):
        logger.debug(event)

    def save_as(self, event):
        options = QFileDialog.Options()

        path, format = QFileDialog.getSaveFileName(
            self, "caption", '',
            "SPSS Statistics (*.sav);;"
            "FatsStat (*.frs)", '', options)

        logger.debug(path)
        logger.debug(format)
        ext = os.path.splitext(path)[1][1:]
        logger.debug(ext)
        writer = Writer(path, Writer.ExtensionsFormat[ext])
        try:
            writer.write()
        except Exception as e:
            logger.error(e)
            QMessageBox.critical(self, "Error", str(e))

