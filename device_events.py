import requests
import json
from credentials import api_key


networkId = ''

API_KEY = api_key() # Call the API Key from credentials Module
#SECRET_KEY = '*****'
BASE_URL = 'https://api.meraki.com/api/v1/'

#Request parameters
url_command = f'networks/{networkId}/devices'

#BASE_URL
request_url = BASE_URL + url_command

def get_events():
    header = {
        'X-Cisco-Meraki-API-Key' : API_KEY,
    }

    r = requests.get(request_url,headers=header)

    result = r.json()
    print(json.dumps(result, indent=2))

get_events()