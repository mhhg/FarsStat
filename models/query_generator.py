import re
from copy import deepcopy
import logging

from models import Column
import models

logger = logging.getLogger("FS")


class QueryGenerator(object):
    def __init__(self, query):
        self.query = query

    @property
    def cols(self):
        return self.query.scanner.cols + self.query.select_scanner.cols

    @property
    def insert(self):
        return models.Query.Insert

    @property
    def select(self):
        if self.query.select:
            select = deepcopy(self.query.select)
            for item in self.query.select_scanner.data:
                col, reg = item['col'], item['re']
                if reg:
                    select = re.sub('(?:%s)' % Column.get(col).name,
                                    'd{}'.format(col), select)

            return models.Query.ComputeSelect.format(select=select)
        else:
            return models.Query.Select

    @property
    def on(self):
        on = "ON "
        _and = " AND "
        for id in self.cols:
            on += models.Query.On.format(id) + _and
        on = on[:-len(_and)]

        return on

    @property
    def where(self):
        if self.query.input:
            where = deepcopy(self.query.input)
            for item in self.query.scanner.data:
                col, reg = item['col'], item['re']
                if reg:
                    where = re.sub('(?:%s)' % Column.get(col).name,
                                   'd{}'.format(col), where)

            return models.Query.Where.format(where=where)
        else:
            return ""

    @property
    def joins(self):
        join = ""
        for id in self.cols:
            join += models.Query.Join.format(id, id, id, id)

        join = join.replace('\n', ' ')

        return join

    def check(self):
        if self.query.status != models.Query.Scanned:
            self.query.error = models.Query.NotScannedError
            return False

        # if self.query.error == models.Query.NoColumnError:
        #     return False
        #
        # if not self.cols:
        #     self.query.error = models.Query.NoColumnError
        #     return False

        return True

    def generate(self):
        logger.debug('Generating query. query={}'.format(self.query))
        sql = ""
        if self.check():
            sql = models.Query.SQL.format(
                select=self.select, joins=self.joins, on=self.on,
                group=models.Query.GroupBy, where=self.where)

            sql = sql.replace('  ', ' ')
            self.query.status = models.Query.Generated
            self.query.sql = sql

        return sql
