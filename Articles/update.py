import json
import requests

headers = {
        "Access-Token":"",
        "Client-Secret":"",
        "Content-Type":"application/json",
        "Accept":"application/json",
        }

url = 'https://api.fortnox.se/3/articles/4/'

data = json.dumps({
                "Article": {
                    "Unit": "100",
                    "ArticleNumber": "4"
                }
            })
        

#resp = requests.get(url, headers=headers).json()
resp = requests.put(url, headers=headers, data=data).json()
print(resp)
