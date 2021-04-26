import requests
import  json
from credentials import api_key

serial = '<SerialNumber>'

API_KEY = api_key() # Call the API Key from credentials Module
#SECRET_KEY = '*****'
BASE_URL = 'https://api.meraki.com/api/v1/'

#Request parameters
url_command = f'/devices/{serial}/reboot'

#BASE_URL
request_url = BASE_URL + url_command

def reboot_device():

    header = {
        'X-Cisco-Meraki-API-Key' : API_KEY,
    }
    r = requests.post(request_url,headers=header)

    results = r.json()
    print(json.dumps(results, indent=2))

reboot_device()
