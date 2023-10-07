import logging
import sys


class Logger():
    def __init__(self, name, encoding='utf-8', level=logging.DEBUG):
        logging.basicConfig(filename='logs/' + name + '.log',
                            encoding=encoding, level=level,
                            format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',
                            datefmt='%Y/%m/%d %I:%M:%S %p')

        self.logger = logging.getLogger(name)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def exception(self, msg):
        self.logger.exception(msg)
