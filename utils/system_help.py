import os


class SystemUtil:
    """
        SystemUtil
    """

    def __init__(self):
        pass

    @staticmethod
    def get_root_path():
        """

        :return:
        """
        return os.path.abspath(os.curdir)
