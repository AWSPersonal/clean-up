import logging

class Logger:

    def info(self, message: str):
        logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
        logging.info(message)

    def warn(self, message: str):
        logging.basicConfig(format='%(levelname)s-%(message)s', level=logging.WARN)
        logging.warning(message)

    def warn(self, message: str):
        logging.basicConfig(format='%(levelname)s-%(message)s', level=logging.WARN)
        logging.warning(message)
