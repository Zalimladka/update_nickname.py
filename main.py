import requests
import random

def get_free_proxies():
    url = "https://www.proxyscan.io/api/proxy?type=http,https"
    response = requests.get(url).json()
    return [f"{proxy['Ip']}:{proxy['Port']}" for proxy in response]

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium-browser"
chrome_options.add_argument("--headless")  # Background mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

proxies = get_free_proxies()
proxy = random.choice(proxies)

proxy_dict = {
    'http': f'http://{proxy}',
    'https': f'http://{proxy}'
}

print("[+] Setting up ChromeDriver")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    print("[+] ChromeDriver initialized successfully")
    response = requests.get('https://facebook.com', proxies=proxy_dict)
    print(response.text)
except Exception as e:
    print(f"[-] Error: {e}")
