import requests
import json

headers = {
        "Access-Token":"",
        "Client-Secret":"",
        "Content-Type":"application/json",
        "Accept":"application/json",
        }

main_url = 'https://api.fortnox.se/3/'

inPut = input('Write api endpoint:')

url = main_url + inPut 

resp = requests.get(url, headers=headers).json()

print(json.dumps(resp, indent=4))