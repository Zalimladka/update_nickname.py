from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# Load cookies
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium-browser"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the browser
driver = webdriver.Chrome(options=chrome_options)

# Open Facebook
driver.get("https://www.facebook.com")

# Add cookies
for cookie_name, cookie_value in cookies.items():
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

# Refresh the page to apply cookies
driver.refresh()

# Extract fb_dtsg
fb_dtsg = driver.execute_script("return document.querySelector('[name=\\\"fb_dtsg\\\"]').value")

if fb_dtsg:
    print("[+] fb_dtsg:", fb_dtsg)
else:
    print("[-] fb_dtsg Not Found")

# Close the browser
driver.quit()
