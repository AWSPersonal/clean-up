"""
Contains list of all services
"""

from services.Lambda import StartLambdaService
from services.S3 import StartS3Service


class StartServices:
    """
    Start All Services
    """

    def __init__(self, region):
        self.region = region
        StartLambdaService(region)
        StartS3Service(region)
