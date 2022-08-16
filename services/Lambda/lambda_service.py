"""
    Lambda Service
"""
import json
from datetime import datetime, timezone

import boto3
import dateutil.parser as date_parser

import utils.config as config
from utils.system_help import SystemUtil


class LambdaService:
    """
    Class to represent Lambda
    """

    __path = ""
    __file_name = ""

    def __init__(self, region):
        self.client = boto3.client("lambda", region_name=region)
        self.__path = "lambda"
        self.__file_name = f"lambda_for_{region}.json"
        self.__system = SystemUtil()
        self.region = region
        self.config = config

    def __list_functions(self):
        return self.client.list_functions()

    def __get_path(self):
        path = self.__system.create_dir(
            self.config.exports_path + "exports," + self.__path
        )
        return path

    def get_response(self):
        """
        Get response from client
        """
        print(self.__list_functions()["Functions"])

    def export_response(self):
        """
        Export the list_functions data to a json file
        """
        function_list: dict = self.__list_functions()["Functions"]
        filtered_data = self.__filter_data("LastModified", function_list)
        if len(filtered_data) >= 1:
            file_path = f"{self.__get_path()}/{self.__file_name}"
            with open(file_path, "w") as outfile:
                json.dump(filtered_data, outfile)

    @staticmethod
    def time_calculator(date_string: str):
        """

        :param date_string:
        :return:
        """
        date_now = datetime.now(timezone.utc)
        date_string = date_parser.isoparse(date_string)
        date_difference = date_now - date_string
        return date_difference.days

    def __filter_data(self, key: str, data: dict):
        return list(filter(lambda x: self.time_calculator(x[key]) > 10, data))
