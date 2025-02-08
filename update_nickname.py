from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriver ka path set karein
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Facebook Messenger login page open karein
driver.get("https://www.facebook.com/messages")
time.sleep(5)  # Thoda rukkar page load hone dein

# Facebook credentials fill karen
email_elem = driver.find_element(By.ID, "email")
pass_elem = driver.find_element(By.ID, "pass")
email_elem.send_keys("aapka_email@example.com")
pass_elem.send_keys("aapka_password")
pass_elem.send_keys(Keys.RETURN)
time.sleep(10)  # Login complete hone ka intezar

# Specific group chat thread par navigate karein
driver.get("https://www.facebook.com/messages/thread/GROUP_THREAD_ID")
time.sleep(5)

# Yahan par aapko sabhi members ke "Edit Nickname" buttons locate karne hain.
# Yeh XPath ya CSS selectors ke through kiya ja sakta hai.
nickname_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Edit Nickname')]")

# Har member ke liye loop chalayein
for btn in nickname_buttons:
    try:
        btn.click()
        time.sleep(1)  # UI update ke liye rukna
        # Input field locate karein jahan naya nickname type karna hai
        input_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter nickname']")
        input_field.clear()
        input_field.send_keys("Naya Nickname")  # Yahan apna desired nickname daalein
        # Save/Set button press karen
        save_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Save') or contains(text(), 'Set')]")
        save_btn.click()
        time.sleep(1)
    except Exception as e:
        print("Error updating a nickname:", e)

# Script complete hone ke baad browser band karen
driver.quit()
