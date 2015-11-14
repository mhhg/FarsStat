import sys

from PyQt5.QtWidgets import QApplication
from utils import handle_exception, setup_logger
from models import fill_random
from gui import MainWindow


NUMBER_OF_ROWS = 10 ** 2
NUMBER_OF_COLS = 10
ROW_OFFSET = 2
COL_OFFSET = 2
VALUES_BUTTON_MAX_WIDTH = 50
VARIABLE_LIST_COLS_WIDTH = 50
VARIABLE_LIST_COL_N_WIDTH = 20
VARIABLE_LIST_COLS_COUNT = 6
N_ROLE = 0
NAME_ROLE = 1
TYPE_ROLE = 2
WIDTH_ROLE = 3
DECIMAL_ROLE = 4
LABEL_ROLE = 5

if __name__ == '__main__':
    sys.excepthook = handle_exception
    setup_logger("FS")
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    app.blockSignals(True)
    fill_random()
    app.blockSignals(False)

    window = MainWindow()
    window.show()

    exit_code = app.exec_()
    sys.exit(exit_code)
