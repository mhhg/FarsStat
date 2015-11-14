import logging
from collections import OrderedDict

from models import Cell, QueryScanner, QueryGenerator, db

logger = logging.getLogger("FS")


class Query(object):
    array = OrderedDict()

    SelectCase = 4
    Compute = 5

    NextID = 0
    DefaultColor = "chocolate"

    Inserted = 0
    Scanned = 1
    Generated = 2
    Executed = 3
    Completed = 4
    ErrorOccurred = 5

    Status = {
        Inserted: 'Inserted',
        Scanned: 'Scanned',
        Generated: 'Generated',
        Executed: 'Executed',
        Completed: 'Completed',
        # ErrorOccurred: 'ErrorOccurred'
    }

    NoError = 10
    NoColumnError = 20
    NotScannedError = 50
    WhereError = 30
    ExecutionError = 40

    error_label = {
        NoError: 'NoError',
        NoColumnError: 'NoColumnError',
        NotScannedError: 'NotScannedError',
        WhereError: 'WhereError',
        ExecutionError: 'ExecutionError',
    }
    Select = "SELECT row as r FROM cells q"
    ComputeSelect = "SELECT row as r, {select} FROM cells q"
    Join = "JOIN (SELECT row as r{}, data as d{} FROM cells q{} WHERE " \
           "column={})"
    On = "(r{} = r)"
    Where = " WHERE {where}"
    GroupBy = " GROUP BY r"
    SQL = "{select} {joins} {on} {where} {group};"

    """
    SELECT row_id as r, d1, d2 FROM cell q
        JOIN (select row_id as r1, _data as d1 FROM cell q1 WHERE col_id = 1)
        JOIN (select row_id as r2, _data as d2 FROM cell q2 WHERE col_id = 2)
    ON (r1 = r) AND (r2 = r) GROUP BY r;
    """

    def __init__(self, input=None, select=None):
        self.id = Query.NextID
        Query.NextID += 1
        self.input = input
        self._sql = str()
        self._status = Query.Inserted
        self._error = Query.NoError
        self.error_string = str()
        self.select = select
        self.result = []
        self.scanner = QueryScanner(self)
        self.select_scanner = QueryScanner(self)
        self.generator = QueryGenerator(self)
        Query.array[self.id] = self

    @classmethod
    def count(cls):
        return len(Query.array)

    @property
    def sql(self):
        return self._sql

    @sql.setter
    def sql(self, value):
        logger.debug("set query sql: {}".format(value))
        self._sql = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        logger.debug("set query status: {}".format(value))
        self._status = value

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, value):
        logger.debug("set query error: {}".format(value))
        self._error = value

    @property
    def status_label(self):
        return Query.Status[self.status]

    def scan(self):
        if not self.has_error():
            logger.debug("attempting to scan query")
            if self.input:
                self.scanner.scan(self.input)

            if self.select:
                self.select_scanner.scan(self.select)

    def generate(self):
        if not self.has_error():
            self.generator.generate()

    def before_execution(self):
        if not self.has_error():
            Cell.insert()

    def after_execution(self):
        if not self.has_error():
            pass

    def has_error(self):
        if self.error != Query.NoError:
            return True
        return False

    def execute(self):
        if self.status is Query.Inserted:
            self.scan()
            self.generate()
            self.before_execution()
            if not self.has_error():
                try:
                    result = db.execute(self.sql).fetchall()
                    if self.select:
                        self.result = {item[0]: item[1] for item in result}
                    else:
                        self.result = [item[0] for item in result]

                    logger.debug(self.result)
                    self.status = Query.Executed
                except Exception as e:
                    self.error_string = str(e)
                    self.error = Query.ExecutionError

            self.after_execution()
            logger.debug(self)

    def delete(self):
        pass

    @classmethod
    def get(cls, index):
        return Query.array.get(index, None)

    def __repr__(self):
        return "<Query (id={}, input={}, select={}, error={}, status={}, " \
               "error_string={})>".format(self.id, self.input, self.select,
                                          Query.error_label[self.error],
                                          self.status_label, self.error_string)
