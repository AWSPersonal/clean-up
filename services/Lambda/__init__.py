"""
Contains list of all services
"""
import threading

from services.Lambda.lambda_service import LambdaService


class StartLambdaService:
    """
    Start Lambda Service
    """

    def __init__(self, region):
        self.region = region
        self.__lambda_process()

    @staticmethod
    def __lambda_process():
        threads = list()
        regions = ["ap-south-1", "us-east-1", "us-east-2"]
        for region in regions:
            service = LambdaService(region)
            x = threading.Thread(target=service.export_response())
            threads.append(x)
            x.start()
