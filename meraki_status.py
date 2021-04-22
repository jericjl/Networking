import requests
import  json
from credentials import api_key

API_KEY = api_key()
#SECRET_KEY = '*****'
BASE_URL = 'https://api.meraki.com/api/v1/'

#Request parameters
url_command = 'organizations/916638/devices/statuses'

#BASE_URL
request_url = BASE_URL + url_command

header = {
    'X-Cisco-Meraki-API-Key' : API_KEY,
}
r = requests.get(request_url,headers=header)

results = r.json()
#print(json.dumps(result, indent=4))

for data in results:   
    # print(data)
    for k,v in data.items():
        if v == '': #Check if equal to value pair
            print(json.dumps(data,indent=2))