"""
    Logger
"""

import logging


class Logger:
    """
    Logger
    """

    @staticmethod
    def info(message: str):
        """

        :param message:
        """
        print_format = "%(levelname)s : %(message)s"
        logging.basicConfig(format=print_format, level=logging.INFO)
        logging.info(message)

    @staticmethod
    def warn(message: str):
        """

        :param message:
        """
        print_format = "%(levelname)s : %(message)s"
        logging.basicConfig(format=print_format, level=logging.WARN)
        logging.warning(message)

    @staticmethod
    def debug(message: str):
        """

        :param message:
        """
        print_format = "%(levelname)s : %(message)s"
        logging.basicConfig(format=print_format, level=logging.DEBUG)
        logging.warning(message)

    @staticmethod
    def error(message: str):
        """

        :param message:
        """
        print_format = "%(levelname)s : %(message)s"
        logging.basicConfig(format=print_format, level=logging.ERROR)
        logging.warning(message)
