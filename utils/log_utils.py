import logging
from logging.config import dictConfig

def setup_logger(name):
    formatter = logging.Formatter(
        fmt='[%(asctime)s] '
            '[Level: %(levelname)s] '
            '[Module: %(module)-25s] '
            '[Line: [%(lineno)-4s] '
            '[Func: %(funcName)-15s] '
            '[Message: %(message)s]')

    # handler = logging.FileHandler('log.txt')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(handler)

    return logger

def config_logger():
    pass