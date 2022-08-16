"""
Config values taken from .env file
"""
import os

from dotenv import load_dotenv

load_dotenv()

exports_path = os.getenv("EXPORTS_PATH") if os.getenv("EXPORTS_PATH") else ""
