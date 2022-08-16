import os

from utils.logger import Logger


class SystemUtil:
    """
    SystemUtil
    """

    def __init__(self):
        self.__logger = Logger()

    def create_dir(self, path_string: str = None):
        path = os.path.join(*path_string.split(","))
        is_exist = os.path.exists(path)
        if not is_exist:
            os.makedirs(path)
            self.__logger.info(f"Successfully created directory: {path}")
        return path
