import requests
from pprint import pprint
from dotenv import load_dotenv
import os

stem = ""
load_dotenv()
key = os.getenv("STUBHUB_KEY")

def get(url):
    print(url)
    resp = requests.get(url)
    print(resp)
    return resp.json()

def get_event()