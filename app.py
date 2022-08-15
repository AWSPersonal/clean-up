from services.lambda_service import LambdaService
import argparse
from utils.logger import Logger


class App:
    """
        Entry class for the program
    """

    __log = Logger()
    __service = LambdaService("us-east-1")
    __parser = argparse.ArgumentParser(description='Short sample app')

    @staticmethod
    def start(self):
        """
        Start the functionality
        """
        self.__log.info("AWS clean up has started...")

        self.parser.add_argument('--export', action="store_true", dest='export', default=False)
        self.parser.add_argument('--response', action="store_true", dest='response', default=False)

        args = self.parser.parse_args()

        if args.export:
            self.__service.export_response()

        if args.response:
            self.__service.get_response()

        if True not in vars(args):
            self.__log.info("AWS clean up Complete!")


if __name__ == "__main__":
    app = App()
    app.start()
