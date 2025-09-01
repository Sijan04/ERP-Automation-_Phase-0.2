
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://amarsolution.xyz/login")
driver.maximize_window()

try:
    driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
except Exception as e:
    print("Not login:", e)

# Keep browser open for 5 minutes
time.sleep(2)
driver.quit()

































