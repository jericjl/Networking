import requests
import  json
from credentials import api_key
from credentials import org_id


API_KEY = api_key() # Call the API Key from credentials Module
#SECRET_KEY = '*****'
BASE_URL = 'https://api.meraki.com/api/v1/'

#Request parameters
url_command = f'organizations/{org_id()}/devices/statuses'

#BASE_URL
request_url = BASE_URL + url_command

def get_equipment(status):
    equipmentstatus = str(status)
    header = {
        'X-Cisco-Meraki-API-Key' : API_KEY,
    }
    r = requests.get(request_url,headers=header)

    results = r.json()
    #print(json.dumps(result, indent=4))
    i = []
    for data in results:   
        # print(data)
        for k,v in data.items():
            if v == equipmentstatus: #Check if equal to value pair
                result =  i.append(data) #append()
    return i

status = input("Please input 'online' or 'offline' equipment : ")
print(json.dumps(get_equipment(status),indent=2))
