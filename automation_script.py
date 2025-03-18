import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

group_id = config["group_id"]
members = config["members"]

# Debugging: Print loaded data
print(f"Group ID: {group_id}")
print(f"Members: {members}")

# Configure Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Optional: To run without a visible browser
driver = webdriver.Chrome(options=options)

# Log in to Facebook
driver.get("https://www.facebook.com")
input("Log in to Facebook manually and press Enter...")

# Navigate to the group
group_url = f"https://www.facebook.com/groups/{group_id}"
driver.get(group_url)
time.sleep(5)  # Wait for the group page to load

# Loop through members and update nicknames
for member in members:
    try:
        # Search for member by ID
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search members']")
        search_box.send_keys(member["id"])
        time.sleep(2)

        # Click on Edit Nickname
        edit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Edit Nickname')]")
        edit_button.click()
        time.sleep(2)

        # Update Nickname
        nickname_input = driver.find_element(By.XPATH, "//input[@name='nickname']")
        nickname_input.clear()
        nickname_input.send_keys(member["nickname"])
        nickname_input.submit()
        print(f"Nickname updated successfully for {member['id']} to {member['nickname']}!")

    except Exception as e:
        print(f"Failed to update nickname for {member['id']}: {e}")

# Quit Driver
driver.quit()
