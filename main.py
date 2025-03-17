import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from undetected_chromedriver import Chrome

# Load config.json file
with open("config.json", "r") as f:
    config = json.load(f)

token = config["token"]
group_id = config["group_id"]
nickname = config["nickname"]

# Selenium Setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/chromium"

# Launch Chrome
driver = Chrome(options=chrome_options)
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
