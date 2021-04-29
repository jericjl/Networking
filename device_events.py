import requests
import json
from credentials import api_key

API_KEY = api_key() # Call the API Key from credentials Module


def get_events(netId):
    
    networkId = netId

    BASE_URL = 'https://api.meraki.com/api/v1/'

    #Request parameters
    url_command = f'networks/{networkId}/events'

    #BASE_URL
    request_url = BASE_URL + url_command
    header = {
        'X-Cisco-Meraki-API-Key' : API_KEY,
    }

    r = requests.get(request_url,headers=header)

    results = r.json()
    return results




netId = input("Please input your Meraki Network ID : ")
events = get_events(netId)

print(json.dumps(events, indent=2))