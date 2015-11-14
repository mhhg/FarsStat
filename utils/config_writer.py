from configparser import ConfigParser
import os
import sys

class ConfigWriter():
    def __init__(self, config = ConfigParser()):
        self.config = ConfigParser()
        self.config['DEFAULT'] = {
            'number-of-rows': 10 ** 2,
            'number-of-columns': 10,
            'row-offset': 2,
            'columns-offset': 2,
        }
        self.config.update(config)

    def write(self):
        with open('fs-config.ini', 'w') as config_file:
            self.config.write(config_file)
