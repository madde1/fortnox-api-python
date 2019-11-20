import json
import requests


headers = {
        "Access-Token":"",
        "Client-Secret":"",
        "Content-Type":"application/json",
        "Accept":"application/json",
        }

url = 'https://api.fortnox.se/3/prices/A/4'

data = json.dumps ({
    "Price": {
        "Price": 129
    }
})

resp = requests.put(url, headers=headers, data=data).json()

print(resp)



