import requests
import json

headers = {
        "Access-Token":"",
        "Client-Secret":"",
        "Content-Type":"application/json",
        "Accept":"application/json",
        }
url = 'https://api.fortnox.se/3/invoices/3'

resp = requests.get(url, headers=headers).json()

print(json.dumps(resp, indent=4))