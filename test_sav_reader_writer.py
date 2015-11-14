from PyQt5.QtWidgets import QFileDialog

from savReaderWriter import SavWriter
from utils import setup_logger

logger = setup_logger("FS")

def write_sav_file(savFileName):
    records = [[b'Test1', 1, 1], [b'Test2', 2, 1]]
    varNames = ['var1', 'v2', 'v3']
    varTypes = {'var1': 5, 'v2': 0, 'v3': 0}

    with SavWriter(savFileName, varNames, varTypes) as writer:
        for record in records:
            writer.writerow(record)

def setSaveFileName():
    logger.debug("hi")
    options = QFileDialog.Options()

    fileName, _ = QFileDialog.getSaveFileName(
        None, "caption", '',
        "All Files (*);;Text Files (*.txt)", '', options)
    logger.debug(fileName)


if __name__ == "__main__":
    setSaveFileName()
