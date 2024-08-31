import requests
from pprint import pprint
from dotenv import load_dotenv
import os

stem = ""
load_dotenv()
key = os.getenv("STUBHUB_KEY")