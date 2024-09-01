from dotenv import load_dotenv
import os

from urllib import parse
import requests

load_dotenv()

api_key = os.getenv('TICKETMASTER_KEY')
event_id = -1

base_url="https://app.ticketmaster.com/discovery/v2/events"
url=f'{base_url}/{event_id}.json?{parse.urlencode([('apikey', api_key)])}'
print(url)

requests.get(url)

#GET /discovery/v2/events.json?apikey=LFxCDAtqoQJlw3r7AZpdQ0kThXIQrEA0&size=1 HTTP/1.1
#Host: app.ticketmaster.com
#X-Target-URI: https://app.ticketmaster.com
#Connection: Keep-Alive


