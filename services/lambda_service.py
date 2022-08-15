"""
    Lambda Service
"""
import json

import boto3
import os
import logging

from utils.system_help import SystemUtil


class LambdaService:
    """
        Class to represent Lambda
    """

    __path = ""
    __file_name = ""

    def __init__(self, region):
        self.client = boto3.client("lambda", region_name=region)
        self.__path = "exports/lambda"
        self.__file_name = "lambda.json"
        self.__system = SystemUtil()

    def __list_functions(self):
        return self.client.list_functions()

    def __get_path(self):
        path = os.path.join(self.__system.get_root_path(), self.__path, self.__file_name)
        is_exist = os.path.exists(path)
        if not is_exist:
            os.makedirs(path)
            logging.info(f'Successfully created directory: ${path}')
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
        json_object = self.__list_functions()
        with open(self.__get_path(), "w") as outfile:
            json.dump(json_object, outfile)
