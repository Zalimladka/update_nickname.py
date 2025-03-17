from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Chrome options
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium-browser"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Driver setup
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
driver.get('https://www.facebook.com')

print(driver.page_source)
