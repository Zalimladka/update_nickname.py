import json
import requests

# Load Cookies from cookies.json
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# Convert cookies to requests format
cookies_str = '; '.join([f"{key}={value}" for key, value in cookies.items()])
headers = {
    'Cookie': cookies_str,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36'
}

# Send Request to m.facebook.com
response = requests.get('https://m.facebook.com/', headers=headers)

# Extract fb_dtsg
if '"fb_dtsg"' in response.text:
    fb_dtsg = response.text.split('"fb_dtsg"')[1].split('value="')[1].split('"')[0]
    print(f"[+] fb_dtsg: {fb_dtsg}")
    
    # Save in cookies.json
    cookies['fb_dtsg'] = fb_dtsg
    with open('cookies.json', 'w') as f:
        json.dump(cookies, f, indent=4)
    print("[+] fb_dtsg successfully saved in cookies.json ✅")
else:
    print("[-] fb_dtsg not found!")
