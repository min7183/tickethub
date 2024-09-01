from dotenv import load_dotenv
import os

from datetime import datetime

from urllib import parse
import requests
from pprint import pprint
    
load_dotenv()
key = os.getenv('TICKETMASTER_KEY')
event_id = -1
stem="https://app.ticketmaster.com/discovery/v2/events"

def get_events(city=None, date=None):
    #obtains list of events based on search filters
    url=f'{stem}.json?{parse.urlencode([('apikey', key)])}'
    if(city):
        url=f'{url}&{parse.urlencode([('city', city)])}'
    if(date):
        url=f'{url}&{parse.urlencode([('localStartEndDateTime', date)])}'
    response = requests.get(url)
    pprint(response.text)

def get_event(event_id):
    #returns info about specific event based on event id
    url=f'{stem}/{event_id}.json?{parse.urlencode([('apikey', key)])}'
    print(url)
    #requests.get(url)

if __name__ == '__main__':
    get_events(city=['Los Angeles'])
#GET /discovery/v2/events.json?apikey=LFxCDAtqoQJlw3r7AZpdQ0kThXIQrEA0&size=1 HTTP/1.1
#Host: app.ticketmaster.com
#X-Target-URI: https://app.ticketmaster.com
#Connection: Keep-Alive


