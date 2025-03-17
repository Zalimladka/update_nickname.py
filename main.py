import requests
import json

with open('token.json', 'r') as f:
    token = json.load(f)['token']

with open('groups.txt', 'r') as f:
    groups = f.read().strip().splitlines()

proxies = open('proxy.txt').read().strip().splitlines()

for group_id in groups:
    url = f"https://graph.facebook.com/{group_id}"
    payload = {
        'name': 'New Group Name',
        'access_token': token
    }
    proxy = {'http': proxies[0], 'https': proxies[0]}
    
    response = requests.post(url, data=payload, proxies=proxy)
    
    if response.status_code == 200:
        print(f"[+] Group Renamed: {group_id}")
    else:
        print(f"[-] Error: {response.text}")
