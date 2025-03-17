import requests

cookies = {
    'c_user': '61573484631602',
    'xs': '5:gfrDLgHvqi00uQ:2:1742097762:-1:10732',
    'fr': '0PBZ9BRBK2g8y3pRi.AWXei5hRq80d8vPSIcrPfW1GBS5aZNyvW8-rQg.Bnzy5l..AAA.0.0.Bn1k9F.AWVg1z2f_-k',
    'datr': 'ZS7PZ9DpPf9oazWHMij9DC-e',
    'sb': 'ZS7PZ86Lu8JdDaFhIIxbM3Fy'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get("https://www.facebook.com/api/graphql/", cookies=cookies, headers=headers)

if "fb_dtsg" in response.text:
    fb_dtsg = response.text.split('"DTSGInitialData",[],{"token":"')[1].split('"')[0]
    print("[+] fb_dtsg:", fb_dtsg)
else:
    print("[-] fb_dtsg Not Found")
