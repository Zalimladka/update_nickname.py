import requests
import json
import re

# Cookie load karna
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get('https://www.facebook.com/', cookies=cookies, headers=headers)

# fb_dtsg ko hidden form me extract karna
fb_dtsg = re.search(r'{"token":"(.*?)"}', response.text)

if fb_dtsg:
    print("[+] fb_dtsg Found:", fb_dtsg.group(1))
else:
    print("[-] fb_dtsg Not Found")
