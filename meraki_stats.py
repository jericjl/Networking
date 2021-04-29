import requests
import  json
from credentials import api_key
from credentials import org_id


API_KEY = api_key() # Call the API Key from credentials Module


def get_equipment(status):
    equipmentstatus = str(status)

    BASE_URL = 'https://api.meraki.com/api/v1/'

    #Request parameters
    url_command = f'organizations/{org_id()}/devices/statuses'
    request_url = BASE_URL + url_command

    header = {
        'X-Cisco-Meraki-API-Key' : API_KEY,
    }
    r = requests.get(request_url,headers=header)

    results = r.json()
    #print(json.dumps(result, indent=4))
    equipment_list = []

    for data in results:   # Extract data from the list
        # print(data)
        for k,v in data.items(): #Extract data from Dictionary
            if v == equipmentstatus: #Check if value is equal to key pair
                result =  i.append(data) 
    return equipment_list

status = input("Please input : ")

print(json.dumps(get_equipment(status),indent=2)) #Print Result from get_equipment function
