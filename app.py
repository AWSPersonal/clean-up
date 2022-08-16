"""
AWS Clean Up Tool lets you terminate resources
that have NOT been used for a very long time
"""

import argparse

from services import StartServices
from utils.logger import Logger


class App:
    """
    Entry class for the program
    """

    def __init__(self):
        self.__start()

    @staticmethod
    def __start():
        """
        Start the functionality
        """
        __log = Logger()
        __parser = argparse.ArgumentParser(description="Short sample app")
        __log.info("AWS clean up has started...")

        __parser.add_argument(
            "--export", action="store_true", dest="export", default=False
        )
        __parser.add_argument(
            "--response", action="store_true", dest="response", default=False
        )

        args = __parser.parse_args()

        # if args.export:
        #     __service.export_response()
        #
        # if args.response:
        #     self.__service.get_response()

        if True not in vars(args):
            __log.info("AWS clean up Complete!")

        StartServices("ap-south-1")


if __name__ == "__main__":
    App()
