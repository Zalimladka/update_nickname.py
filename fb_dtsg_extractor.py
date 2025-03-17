from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

# Cookies ko load karna
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

# Chrome headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Browser open
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.facebook.com')

# Cookies inject karna
for cookie in cookies:
    driver.add_cookie({
        'name': cookie,
        'value': cookies[cookie],
        'domain': '.facebook.com'
    })

# Page ko reload karna
driver.get('https://www.facebook.com')

# Thoda wait karo (important)
time.sleep(5)

# fb_dtsg ko extract karna
fb_dtsg = driver.find_element(By.NAME, 'fb_dtsg').get_attribute('value')

if fb_dtsg:
    print("[+] fb_dtsg Found:", fb_dtsg)
else:
    print("[-] fb_dtsg Not Found")

# Browser ko band karna
driver.quit()
