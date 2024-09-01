import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import urllib.parse
import base64

stem = "https://api.stubhub.net/"
load_dotenv()
key = os.getenv("STUBHUB_KEY")

# def get(url : str)->str:
#     print(url)
#     resp = requests.get(url)
#     print(resp)
#     return resp.json()

def get_authentication(client_id, client_secret)->str:
    encoded_client_id = urllib.parse.quote(client_id, safe='')
    encoded_client_secret = urllib.parse.quote(client_secret, safe='')

    # Concatenate with a colon
    concatenated_string = f"{encoded_client_id}:{encoded_client_secret}"

    # Base64 encode the concatenated string
    base64_encoded = base64.b64encode(concatenated_string.encode('utf-8')).decode('utf-8')

    print(base64_encoded)
    return(base64_encoded)


def get_event(
    q=None,
    dateLocal=None,
    page=1,
    page_size=10,
    updated_since=None,
    sort=None,
    min_resource_version=None,
    country_code=None,
    latitude=None,
    longitude=None,
    max_distance_in_meters=None,
    genre_id=None,
    exclude_parking_passes=None
    ):

    params = {
        'q': q,
        'dateLocal': dateLocal,
        'page': page,
        'page_size': page_size,
        'updated_since': updated_since,
        'sort': sort,
        'min_resource_version': min_resource_version,
        'country_code': country_code,
        'latitude': latitude,
        'longitude': longitude,
        'max_distance_in_meters': max_distance_in_meters,
        'genre_id': genre_id,
        'exclude_parking_passes': exclude_parking_passes
    }

    st = stem + "catalog/events/search"
    params = {key: value for key, value in params.items() if value is not None}

    response = requests.get(st, params=params, cert = key)

    if response.status_code == 200:
        pprint(response)
        return response.json()
    else:
        response.raise_for_status()
    

def main()->None:
    get_event(q="concert",
            dateLocal="2024-08-31T00:00:00Z",
            page=1,
            page_size=20,
            updated_since="2024-08-30T00:00:00Z",
            sort="resource_version",
            country_code="US",
            latitude=37.7749,
            longitude=-122.4194,
            max_distance_in_meters=5000,
            genre_id=1,
            exclude_parking_passes=True)    

if __name__ == '__main__':
    main()


# q	
# string or null
# The query text to be used to match events.

# dateLocal	
# string or null <date-time>
# The specific date of the event, this is optional

# page	
# integer <int32>
# Specifies which page of data to retrieve.

# page_size	
# integer <int32>
# Set custom page sizes on response.

# updated_since	
# string <date-time>
# Filters the response to only return items that have been updated since the given timestamp

# sort	
# string
# Determines the ordering of items. A comma-separated string containing resource_version.

# min_resource_version	
# integer or null <int64>
# country_code	
# string
# Filters results to only include events located in the specified country.

# latitude	
# number or null <double>
# When provided with longitude and distance filters events returned to ones within the specified distance of the lat/long.

# longitude	
# number or null <double>
# When provided with latitude and distance filters events returned to ones within the specified distance of the lat/long.

# max_distance_in_meters	
# integer or null <int32>
# When provided with latitude and longitude filters events returned to ones within the specified distance of the lat/long.

# genre_id	
# integer or null <int32>
# Filters results to only include events for the specified genre id.

# exclude_parking_passes	
# boolean or null
# Filters results to remove parking passes