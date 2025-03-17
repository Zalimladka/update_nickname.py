import requests
import json
import undetected_chromedriver as uc
import chromedriver_autoinstaller

# Load config.json
with open("config.json", "r") as f:
    config = json.load(f)

token = config["token"]
group_id = config["group_id"]
nickname = config["nickname"]

# Install correct Chrome Driver
chromedriver_autoinstaller.install()

# Launch Undetected Chrome
driver = uc.Chrome(headless=True)
driver.get(f"https://graph.facebook.com/{group_id}?access_token={token}")

# Change Nickname API Request
url = f"https://graph.facebook.com/{group_id}/nicknames"
data = {
    "nickname": nickname,
    "access_token": token
}
response = requests.post(url, data=data)

if "error" in response.text:
    print("[-] Failed to Change Nickname!")
else:
    print("[+] Nickname Changed Successfully!")

driver.quit()
