import json
import requests

# Load your cookies
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# Set Headers for Facebook
headers = {
    'authority': 'www.facebook.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'accept': '*/*'
}

# Send Request to Facebook
response = requests.get('https://www.facebook.com/', cookies=cookies, headers=headers)

# fb_dtsg Extract
fb_dtsg = response.text.split('"fb_dtsg"')[1].split('value="')[1].split('"')[0]

# Save fb_dtsg in JSON
cookies['fb_dtsg'] = fb_dtsg

with open('cookies.json', 'w') as f:
    json.dump(cookies, f, indent=4)

print("[+] fb_dtsg Successfully Extracted:", fb_dtsg)
