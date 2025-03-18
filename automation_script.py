from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Headless mode (optional)
driver = webdriver.Chrome(options=options)

# Log in to Facebook
driver.get("https://www.facebook.com")
print("Please manually log in to Facebook in the opened browser...")
time.sleep(30)  # Wait for manual login

# Navigate to the group
group_url = "https://www.facebook.com/groups/123456789"
driver.get(group_url)
time.sleep(5)  # Wait for group page to load

# Example action: Changing a nickname
try:
    member_search = driver.find_element(By.XPATH, "//input[@placeholder='Search members']")
    member_search.send_keys("100089237957268")  # Replace with member details
    time.sleep(2)

    edit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Edit Nickname')]")
    edit_button.click()
    time.sleep(2)

    nickname_input = driver.find_element(By.XPATH, "//input[@name='nickname']")
    nickname_input.clear()
    nickname_input.send_keys("New Nickname")
    nickname_input.submit()
    print("Nickname updated successfully!")
except Exception as e:
    print(f"Error occurred: {e}")

driver.quit()
