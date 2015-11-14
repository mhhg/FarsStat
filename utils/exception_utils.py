import sys
import logging

def handle_exception(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger("FS")
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Uncaught exception",
                    exc_info=(exc_type, exc_value, exc_traceback))
