import re
import logging

from models import Column
import models
logger = logging.getLogger("FS")


class QueryScanner(object):
    def __init__(self, query):
        self.query = query
        self.data = []
        self._cols = []

    @property
    def cols(self):
        return self._cols

    def scan(self, input):
        logger.debug('scanning query. query={}'.format(self.query))
        for col in Column.array:
            self.data.append({
                'col': col,
                're': re.search('(?:%s)' % Column.get(col).name,
                                input)})
        cols = [item['col'] for item in self.data if item['re']]
        for column in cols:
            logger.debug(column)
        if not cols:
            self.query.error = models.Query.NoColumnError
        self.query.status = models.Query.Scanned
        self._cols = cols
