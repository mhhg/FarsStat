import logging
import sys

for x in sys.path: print(x)
from models import Cell, Column

logger = logging.getLogger("FS")


class Writer(object):
    DB = 1
    SAV = 2
    CSV = 3
    XLSX = 4
    PDF = 5

    FormatsDetail = {
        DB: "Database",
        SAV: "IBM SPSS Statistics",
        CSV: "Comma Separated Values",
        XLSX: "Excel Workbook",
        PDF: "PDF Document",
    }

    FormatsExtension = {
        DB: 'db',
        SAV: "sav",
        CSV: "csv",
        XLSX: "xlsx",
        PDF: "pdf",
    }

    ExtensionsFormat = {ext: fmt for fmt, ext in FormatsExtension.items()}

    def __init__(self, path, format):
        self.path = path
        self.format = format

    def write(self):
        if self.format == Writer.SAV:
            self.write_as_sav()

    def write_as_sqlite_db(self):
        pass

    def write_as_sav(self):
        records = Cell.to_records()
        columns_name = Column.names_list()
        columns_type = Column.data_types_list()
        path = self.path
        
    def write_as_xlsx(self):
        pass

    def write_as_pdf(self):
        pass
