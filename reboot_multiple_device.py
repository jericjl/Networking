import requests
import  json
from credentials import api_key


def reboot_devices(serial_numbers):
    sn = serial_numbers
    API_KEY = api_key() # Call the API Key from credentials Module
    
    header = {
        'X-Cisco-Meraki-API-Key' : API_KEY,
    }

    BASE_URL = 'https://api.meraki.com/api/v1'
    
    stats = []  
    #request_url = BASE_URL + url_command
    for serial in sn:

        #Request parameters
        url_command = f'/devices/{serial}/reboot' #use this to reboot devices
                        #'/devices/{serial}/blinkLeds'  #use this to blink led in devices

        request_url = BASE_URL + url_command
        r = requests.post(request_url,headers=header) #Execute request
        result = r.json()
        result.update(SN = serial) #Add key value pair to dictionary
        stats.append(result)
    return stats



serials = ['<Serial number>', '<Serial number>']
status = reboot_devices(serials)
print(json.dumps(status, indent=2))